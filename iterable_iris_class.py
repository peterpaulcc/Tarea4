import pandas as pd

# Clase IterableIris

class IterableIris:
    def __init__(self, file_path):
        self.df = pd.read_csv(file_path)
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.df):
            print("error")
            raise StopIteration
        else:
            result = self.df.iloc[self.index:self.index+2]
            self.index += 2
            return result

# Prueba de la clase
if __name__ == "__main__":
    iris_iterable = IterableIris("iris.csv")
    while True:
        try:
            print(next(iris_iterable))
        except StopIteration:
            break