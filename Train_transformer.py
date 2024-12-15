from happytransformer import HappyTextToText, TTTrainArgs
import pandas as pd

happy_tt = HappyTextToText("T5", "t5-base")

def preprocess_csv(file_path):
    try:
        df = pd.read_csv(file_path)
        df["input"] = df["input"].str.slice(0, 512)
        df["target"] = df["target"].str.slice(0, 512) 
        clean_file_path = "clean_train.csv"
        df.to_csv(clean_file_path, index=False)
        return clean_file_path
    except Exception as e:
        print(f"Error during preprocessing: {e}")
        return None


def _Train_():
    try:
        clean_file = preprocess_csv("train.csv")
        if not clean_file:
            print("Dataset preprocessing failed.")
            return
        args = TTTrainArgs(
            batch_size=4,
            num_train_epochs=3,
            max_input_length=128,
            max_output_length=128 
        )
        
        happy_tt.train(clean_file, args=args)
        print("Training completed successfully.")
    except FileNotFoundError:
        print("Error: train.csv file not found. Please provide the correct path.")
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

