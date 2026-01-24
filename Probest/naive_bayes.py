# ======================================================
# 🌸 Ejemplo: Clasificación con Naive Bayes (Iris)
# ======================================================

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, classification_report

# 1️⃣ Cargar dataset Iris
iris = load_iris()
X = iris.data      # 4 características
y = iris.target    # 3 clases de flores

# 2️⃣ Dividir datos
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 3️⃣ Crear y entrenar el modelo
modelo = GaussianNB()
modelo.fit(X_train, y_train)

# 4️⃣ Hacer predicciones
y_pred = modelo.predict(X_test)

# 5️⃣ Evaluar resultados
print("✅ Precisión del modelo:", accuracy_score(y_test, y_pred))
print("\n📊 Reporte de clasificación:\n", classification_report(y_test, y_pred))

