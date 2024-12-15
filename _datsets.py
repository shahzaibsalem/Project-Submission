from datasets import load_dataset

def _import_datasets():
    train_dataset = load_dataset("jfleg", split='validation[:]')
    eval_dataset = load_dataset("jfleg", split='test[:]')
    return train_dataset, eval_dataset
