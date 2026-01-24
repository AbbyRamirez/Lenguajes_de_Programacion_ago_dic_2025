
# 1️⃣ Importar librerías necesarias
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# 2️⃣ Cargar el dataset Iris
iris = load_iris()
X = iris.data       # características (4 variables)
y = iris.target     # etiquetas (tipo de flor)
target_names = iris.target_names

print("Características:", iris.feature_names)
print("Clases:", target_names, "\n")

# 3️⃣ Escalar los datos (muy importante para PCA)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 4️⃣ Aplicar PCA para reducir de 4D a 2D
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# 5️⃣ Crear un DataFrame con los resultados
df_pca = pd.DataFrame(X_pca, columns=['PC1', 'PC2'])
df_pca['Clase'] = y

print("📋 Primeras filas del dataset transformado:")
print(df_pca.head(), "\n")

# 6️⃣ Visualizar el resultado del PCA
plt.figure(figsize=(8,6))
colors = ['red', 'green', 'blue']

for color, i, target_name in zip(colors, [0, 1, 2], target_names):
    plt.scatter(df_pca.loc[df_pca['Clase'] == i, 'PC1'],
                df_pca.loc[df_pca['Clase'] == i, 'PC2'],
                color=color, alpha=0.7, label=target_name, edgecolor='k')

plt.legend()
plt.title('🌸 Reducción de Dimensionalidad con PCA (Iris Dataset)')
plt.xlabel('Componente Principal 1')
plt.ylabel('Componente Principal 2')
plt.grid(True)
plt.show()

# 7️⃣ Mostrar cuánta información conserva el PCA
print("📈 Varianza explicada por cada componente:")
print(pca.explained_variance_ratio_)
print(f"\n🔹 Varianza total explicada: {pca.explained_variance_ratio_.sum():.2f}")


