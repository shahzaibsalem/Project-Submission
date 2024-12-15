import csv
from datasets import load_dataset
from happytransformer import TTSettings, TTTrainArgs, HappyTextToText
from  _datsets import _import_datasets
happy_tt = HappyTextToText("T5", "t5-base")
train_dataset, eval_dataset = _import_datasets()

print("Training Dataset Sample:", train_dataset[0])
print("Evaluation Dataset Sample:", eval_dataset[0])
