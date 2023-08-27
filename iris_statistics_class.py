import pandas as pd
import matplotlib.pyplot as plt

# Clase IrisStatistics

class IrisStatistics:
    def __init__(self, file_path):
        self.df = pd.read_csv(file_path)

    def basic_statistics(self):
        return self.df.describe()

    def available_variables(self):
        return self.df.columns.tolist()

    def variable_statistics(self, variable):
        if variable not in self.df.columns:
            return "Variable no disponible"
        
        stats = self.df[variable].describe(percentiles=[.25, .5, .75])
        plt.hist(self.df[variable], bins=20)
        plt.title(f"Histograma de {variable}")
        plt.xlabel(variable)
        plt.ylabel("Frecuencia")
        plt.show()
        return stats

# Prueba de la clase
if __name__ == "__main__":
    iris_stats = IrisStatistics("iris.csv")
    print(iris_stats.basic_statistics())
    print(iris_stats.available_variables())
    print(iris_stats.variable_statistics("sepal.length"))