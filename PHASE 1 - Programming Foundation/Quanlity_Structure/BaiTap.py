from dataclasses import dataclass

@dataclass
class LLMConfig:
    model_name: str
    temperature: float
    max_tokens: int

    def initialize_model(self) -> bool:
        print(
            f"Model {self.model_name} initialized "
            f"with temperature {self.temperature} "
            f"and max tokens {self.max_tokens}"
        )
        return True

if __name__ == "__main__":
    config = LLMConfig("BaiTap", 10, 5)
    print(config.initialize_model())