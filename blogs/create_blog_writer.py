import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process, LLM
from llm_model import LLMModel
from llm_type import LLMType

class CreateBlogWriter:
    
    def __init__(self, type):
        load_dotenv ()
        llm_model = LLMModel()
        self.llm = (
          llm_model.open_ai_gpt_4o_mini() if LLMType(type) == LLMType.OPEN_AI_GPT_4O_MINI 
          else llm_model.deepseek(os.getenv("DEEPSEEK_API_KEY")) if LLMType(type) == LLMType.DEEPSEEK
          else llm_model.ollama_deepseek()
        )
        self.create_crew()

    def create_crew(self):
      """
       Agentes
      """
      self.planner = Agent(
        role = "Planejador de Conteúdo",
        goal = "Planejar conteúdo envolvente e factualmente preciso sobre {topic}",
        backstory = "Você está trabalhando no planejamento de um artigo de blog "
                    "sobre o tema: {topic} no 'https://medium.com/'."
                    "Você coleta informações que ajudam o "
                    "público a aprender algo e tomar decisões informadas. "
                    "Você precisa preparar um esboço detalhado "
                    "com os tópicos e subtópicos relevantes que devem fazer parte do artigo de blog."
                    "Seu trabalho é a base para o Redator de Conteúdo escrever um artigo sobre este tema.",
        llm = self.llm, 
        allow_delegation = False,
        verbose = True
      )

      self.writer = Agent(
        role =  "Redator de Conteúdo",
        goal =  "Escrever um artigo de opinião perspicaz e factualmente preciso "
                "sobre o tema: {topic}",
        backstory = "Você está trabalhando na escrita de um "
                    "novo artigo de opinião sobre o tema: {topic} no 'https://medium.com/'. "
                    "Você baseia sua escrita no trabalho do Planejador de Conteúdo, que fornece um esboço e contexto relevante sobre o tema. "
                    "Você segue os principais objetivos e direção do esboço, conforme fornecido pelo Planejador de Conteúdo. "
                    "Você também fornece insights objetivos e imparciais e os embasa com informações fornecidas pelo Planejador de Conteúdo. "
                    "Você reconhece em seu artigo de opinião quando suas afirmações são opiniões e não declarações objetivas.",
        allow_delegation = False,
        llm = self.llm, 
        verbose = True
      )

      self.editor = Agent(
        role = "Editor",
        goal =  "Editar um post de blog dado para alinhar com "
                "o estilo de escrita da organização 'https://medium.com/'. ",
        backstory = "Você é um editor que recebe um post de blog do Redator de Conteúdo. "
                    "Seu objetivo é revisar o post de blog para garantir que ele siga as melhores práticas jornalísticas,"
                    "forneça pontos de vista equilibrados ao apresentar opiniões ou afirmações, "
                    "e também evite tópicos controversos ou opiniões, sempre que possível.",
        llm = self.llm, 
        allow_delegation = False,
        verbose = True
      )
      """
       Tarefas
      """
      self.plan = Task(
        description = (
        "1. Priorize as últimas tendências, principais players, "
        "e notícias relevantes sobre {topic}.\n"
        "2. Identifique o público-alvo, considerando "
        "seus interesses e pontos de dor.\n"
        "3. Desenvolva um esboço detalhado do conteúdo, incluindo "
        "uma introdução, pontos principais e uma chamada para ação.\n"
        "4. Inclua palavras-chave de SEO e dados ou fontes relevantes."
        ),
        expected_output = "Um documento de plano de conteúdo abrangente "
                          "com um esboço, análise do público, palavras-chave de SEO e recursos.",
        agent = self.planner,
      )

      self.write = Task(
        description = (
        "1. Use o plano de conteúdo para criar um post de blog envolvente "
        "sobre {topic}.\n"
        "2. Incorpore palavras-chave de SEO de forma natural.\n"
        "3. As seções/Subtítulos são nomeadas de forma apropriada "
        "e envolvente.\n"
        "4. Certifique-se de que o post esteja estruturado com uma "
        "introdução envolvente, corpo perspicaz, "
        "e uma conclusão resumida.\n"
        "5. Revise erros gramaticais e "
        "alinhamento com a voz da marca.\n"
        ),
        expected_output = "Um post de blog bem escrito "
                          "em formato markdown, pronto para publicação, cada seção deve ter 2 ou 3 parágrafos.",
        agent = self.writer,
      )

      self.edit = Task(
        description = ( "Revise o post de blog dado para verificar "
                        "erros gramaticais e alinhamento com a voz da marca."),
        expected_output = "Um post de blog bem escrito em formato markdown, "
                          "pronto para publicação, cada seção deve ter 2 ou 3 parágrafos.",
        agent = self.editor
      )
      """
        Crew
      """
      self.crew = Crew(
      agents = [self.planner, self.writer, self.editor],
      tasks = [self.plan, self.write, self.edit],
      process = Process.sequential,
      verbose = True
      )

    def kickoff(self, topic):
        result = self.crew.kickoff(inputs={"topic":topic})
        return result