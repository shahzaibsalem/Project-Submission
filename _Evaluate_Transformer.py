from happytransformer import HappyTextToText
happy_tt = HappyTextToText("T5", "t5-small")

def evaluate():
    try:
        before_result = happy_tt.eval("eval.csv")
        print(before_result.loss)
    except FileNotFoundError:
        print("Error: eval.csv file not found. Please provide the correct path.")
    except AttributeError:
        print("Error: 'loss' attribute not found in the evaluation result.")
    except Exception as e:
        print("An unexpected error occurred:", str(e))