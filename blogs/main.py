
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from llm_type import LLMType
from blogs.create_blog_writer import CreateBlogWriter

create_blog_writer = CreateBlogWriter(LLMType.OLLAMA_DEEPSEEK)
result = create_blog_writer.kickoff('Agentes Inteligentes')
print('################ Saída ################')
print(result)