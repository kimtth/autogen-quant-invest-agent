from textwrap import dedent
from typing import Dict
from autogen import ConversableAgent
from utils.const import DATASET_STOCK, DATASET_SIGNALS
import autogen

class SignalAnalysisAgent:
    def __init__(self, llm_config: Dict):
        self.__llm_config = llm_config
        self.__custom_signal_analysis_agent_prompt = self._custom_signal_analysis_agent_prompt()

    @staticmethod
    def _custom_signal_analysis_agent_prompt() -> str:
        return dedent(
            f"""
            # Role:
            You are responsible for using the `ta` library to create python code for generating buy and sell signals for the stock investing.
            
            # Tasks:
            1. Do not create the code for stock data fetching. The `{DATASET_STOCK}` file will be provided by the `stock_analysis_agent`.
            2. Do not execute the code. Provide the code to the `user_proxy` for execution.
            3. Do not explain why the code is written in a specific way. Do not explain why.
            4. Do not include the code for backtesting the strategy.
            5. Create only python function `generate_signals`.  Do not create other function.
            6. Include the columns `BuySignal`, `SellSignal`, and `Description` in the DataFrame.
            7. Use "Adj Close" exclusively as the price column for generating signals. Never use "Close".
                - Never use `df["Close"]` or `df['Close']` in the code.
                - Use `df["Adj Close"]` or `df['Adj Close']` instead.
            8. Use `ta` library document in the following link: https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html
            9. Use the following code template for importing libraries and defining variables:  
                ```
                import ta
                import pandas as pd
                import os

                WORK_DIR = '.'
                INPUT_FILE = {DATASET_STOCK}
                OUTPUT_FILE = {DATASET_SIGNALS}

                abs_path = os.path.abspath(WORK_DIR)
                ```

            **Example 1:**

            - Input:
                Generate buy/sell signals using MACD and 10 days Moving Average.

            - Function:
                ```python
                import ta
                import pandas as pd
                import os   

                WORK_DIR = '.'
                INPUT_FILE = {DATASET_STOCK}
                OUTPUT_FILE = {DATASET_SIGNALS}

                abs_path = os.path.abspath(WORK_DIR)

                def generate_signals():
                    try:
                        file_input_path = os.path.join(abs_path, INPUT_FILE)
                        df = pd.read_csv(file_input_path)

                        df["MA10"] = ta.trend.sma_indicator(df["Adj Close"], window=10)
                        df["MACD"] = ta.trend.MACD(df["Adj Close"])
                        df["BuySignal"] = (df["Adj Close"] > df["MA10"]) & (df["MACD"] > 0)
                        df["SellSignal"] = (df["Adj Close"] < df["MA10"]) & (df["MACD"] < 0)
                        df["Description"] = "Generated signals using MACD and Moving Average 10 days"

                        df["BuySignal"] = df["BuySignal"].fillna(False)
                        df["SellSignal"] = df["SellSignal"].fillna(False)
                        
                        df_output = df[["BuySignal", "SellSignal", "Description"]]

                        file_output_path = os.path.join(abs_path, OUTPUT_FILE),
                        df_output.to_csv(file_output_path, index=False)   

                        print(f"Signals generated and saved to {{file_output_path}}")
                    except Exception as e:
                        raise Exception(f"An unexpected error occurred: {{e}}")
                
                generate_signals()
                ```
            """
        )

    def create_agent(self) -> ConversableAgent:
        return autogen.AssistantAgent(
            name="custom_signal_analysis_agent",
            system_message=self.__custom_signal_analysis_agent_prompt,
            llm_config=self.__llm_config,
        )