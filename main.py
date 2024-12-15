import csv
from datasets import load_dataset
from happytransformer import TTSettings, TTTrainArgs, HappyTextToText
from  _datsets import _import_datasets
from generate_CSV import CSV_Generator
from _Evaluate_Transformer import evaluate
from Train_transformer import _Train_

happy_tt = HappyTextToText("T5", "t5-base")

def extract_save_datasets():
    train_dataset, eval_dataset = _import_datasets()
    return train_dataset, eval_dataset

def datsets_to_csv():
    train_dataset, eval_dataset = extract_save_datasets()
    CSV_Generator("train.csv", train_dataset)   
    CSV_Generator("eval.csv", eval_dataset)    

# datsets_to_csv()
print("Before Training:")
evaluate()
print("After Training:")
_Train_()
evaluate()

beam_settings = TTSettings(num_beams=5, min_length=1, max_length=20)

example_1 = "grammar: This sentences, has bads grammar and spelling!"
result_1 = happy_tt.generate_text(example_1, args=beam_settings)
print("Corrected Sentence:", result_1.text)

