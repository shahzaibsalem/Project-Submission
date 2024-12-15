from datasets import load_dataset
def _import_datasets():
    train_dataset = load_dataset("jfleg", split='validation[:]')
    eval_dataset = load_dataset("jfleg", split='test[:]')
    train_dataset.save_to_disk("./train_dataset")
    eval_dataset.save_to_disk("./eval_dataset")
    return train_dataset, eval_dataset
