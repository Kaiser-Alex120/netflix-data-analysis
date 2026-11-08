# Vamos a limpiar los datos y obtenerlos para limpiarlos y obtenerlos para su posterior análisis.

from pathlib import Path   # Nos ayuda a construir rutas de archivos de forma segura (funciona en Windows, Mac, Linux)
import pandas as pd        # Librería principal para manejar datos en tablas (DataFrames)
import numpy as np         # Librería para cálculos numéricos (la usarás más adelante en la limpieza)

RAW_DATA_PATH = Path(__file__).resolve().parents[2] / "data" / "raw" / "netflix_titles.csv"

df = pd.read_csv(RAW_DATA_PATH)

df.info()  # Nos da un resumen de los datos, incluyendo el número de filas, columnas y tipos de datos.
print(df.head(3))

# Missing data

for i in df.columns:
    # Recorre cada columna del DataFrame (i = nombre de la columna)
    
    null_rate = df[i].isna().sum() / len(df) * 100
    # df[i].isna()       -> devuelve True/False por cada fila (True = es nulo)
    # .sum()              -> cuenta cuántos True hay (total de nulos en esa columna)
    # len(df)             -> número total de filas del DataFrame
    # división * 100      -> convierte la proporción en porcentaje
    
    if null_rate > 0:
        # Solo imprime si la columna SÍ tiene nulos (evita mostrar columnas con 0%)
        print("{} null rate: {}%".format(i, round(null_rate, 2)))
        # round(null_rate, 2) -> redondea a 2 decimales para que se vea limpio

# Replacements

# Rellena 'country' con el valor MÁS FRECUENTE (la moda), no con "Desconocido"
# .mode()[0] = el país que más se repite en toda la columna
df['country'] = df['country'].fillna(df['country'].mode()[0])

# Rellena 'cast' y 'director' con el texto "No Data"
# .replace(np.nan, 'No Data') es otra forma de hacer lo mismo que .fillna()
df['cast'].replace(np.nan, 'No Data', inplace=True)
df['director'].replace(np.nan, 'No Data', inplace=True)

# Drops
# TODAS las filas que todavía tengan algún nulo restante
# (esto cubre date_added, rating y duration, que no fueron tratadas arriba)
df.dropna(inplace=True)

# Drop Duplicates

# Elimina filas 100% duplicadas (todas las columnas iguales)
df.drop_duplicates(inplace=True)

####################################################################################
# Verificación 1: ¿quedan nulos?
# Debería imprimir una Serie con puros 0
print("Nulos por columna:")
print(df.isnull().sum())
# Verificación 2: ¿quedan duplicados?
# .duplicated() devuelve True/False por fila, .sum() cuenta los True
print("Cantidad de filas duplicadas:", df.duplicated().sum())
# Verificación 3: ¿cuántas filas quedaron después de la limpieza?
# shape devuelve (filas, columnas)
print("Forma del DataFrame (filas, columnas):", df.shape)
# Verificación 4: revisa los tipos de datos finales
print(df.dtypes)
# Verificación 5: un vistazo rápido a los datos
print(df.head(3))
print(df.info())

##############################################################


# Convierte el texto a una fecha real de pandas
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
#  duration tampoco debe aparecer separada
df['duration_int'] = df['duration'].str.extract(r'(\d+)').astype(float)
df['duration_type'] = df['duration'].str.extract(r'([a-zA-Z]+)')

# Qcols_texto = df.select_dtypes(include='object').columns
cols_texto = df.select_dtypes(include='object').columns
df[cols_texto] = df[cols_texto].apply(lambda x: x.str.strip())
# Extraer año y mes de date_added (útil para analizar tendencias por año)
df['year_added'] = df['date_added'].dt.year
df['month_added'] = df['date_added'].dt.month




# Confirmar los tipos de datos finales (clave: date_added debe ser datetime, duration_int debe ser float)
print("Tipos de datos:")
print(df.dtypes)
print()

# 4. Confirmar que date_added se convirtió bien (revisa que no haya NaT en exceso)
print("Nulos en date_added tras conversión:", df['date_added'].isna().sum())
print("Rango de fechas:", df['date_added'].min(), "a", df['date_added'].max())
print()

# 5. Confirmar que duration se separó correctamente
print("Ejemplo de duration separada:")
print(df[['duration', 'duration_int', 'duration_type']].head(5))
print()

# 6. Confirmar valores únicos de duration_type (debería ser solo 'min', 'Season', 'Seasons')
print("Valores únicos en duration_type:", df['duration_type'].unique())
print()

# 7. Forma final del DataFrame
print("Forma final (filas, columnas):", df.shape)
print()

# 8. Vista general de las primeras filas
print(df.head(3))



df.to_csv('data/processed/netflix_titles_clean.csv', index=False)
