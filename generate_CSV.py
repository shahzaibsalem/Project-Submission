import csv
def CSV_Generator(csv_path, dataset):
     with open(csv_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["input", "target"])
        for case in dataset:
            input_text = "grammar: " + case["sentence"]
            for correction in case["corrections"]:
                if input_text and correction:
                    writer.writerow([input_text, correction])