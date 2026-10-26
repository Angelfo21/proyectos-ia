import numpy as np
from sklearn.linear_model import LinearRegression

def regresion_lineal():
    # Datos de entrenamiento de ejemplo (X = años de experiencia, y = salario)
    X = np.array([[1], [2], [3], [4], [5]])
    y = np.array([30000, 40000, 50000, 60000, 70000])

    # Inicializar y entrenar el modelo
    modelo = LinearRegression()
    modelo.fit(X, y)

    # Predecir el salario para 6 años de experiencia
    años_nuevos = np.array([[6]])
    prediccion = modelo.predict(años_nuevos)

    print("--- Modelo de Regresión Lineal ---")
    print(f"Coeficiente (Pendiente): {modelo.coef_[0]:.2f}")
    print(f"Intercepción: {modelo.intercept_:.2f}")
    print(f"Predicción para 6 años de experiencia: ${prediccion[0]:.2f}")

if __name__ == "__main__":
    regresion_lineal() 