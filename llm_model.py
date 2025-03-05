from crewai import LLM

class LLMModel:
    
    def ollama_deepseek(self):
       return LLM(model = "ollama/deepseek-r1:8b",base_url = "http://localhost:11434")
    
    def open_ai_gpt_4o_mini(self):
      return LLM(model="openai/gpt-4o-mini", temperature=0.7)
    
    def deepseek(self, deepseek_api_key):
      return LLM(model="deepseek/deepseek-chat", api_key=deepseek_api_key, temperature=0.7)
  