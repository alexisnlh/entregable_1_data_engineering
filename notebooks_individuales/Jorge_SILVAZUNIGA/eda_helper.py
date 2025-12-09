 #%%writefile data_exploration.py
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def resumen_categorico(df, col, target, mostrar_grafico=True):
    """
    Genera tabla de frecuencias absolutas y relativas para columnas categóricas
    y opcionalmente muestra un violinplot contra una variable numérica (target).
    
    Parámetros:
    -----------
    df : pd.DataFrame
        DataFrame de entrada
    col : str
        Nombre de la columna categórica
    target : str
        Nombre de la columna numérica para comparar en el violinplot
    mostrar_grafico : bool, opcional
        Si True, muestra el gráfico (default=True)
    
    Retorna:
    --------
    resumen : pd.DataFrame
        Tabla con frecuencias absolutas y relativas
    """
    
    # Calcular frecuencias
    freq_abs = df[col].value_counts(dropna=False)
    freq_rel = df[col].value_counts(normalize=True, dropna=False) * 100
    
    # Crear DataFrame resumen ordenado
    resumen = pd.DataFrame({
        "Frecuencia Absoluta": freq_abs,
        "Frecuencia Relativa (%)": freq_rel.round(2)
    }).sort_values(by="Frecuencia Absoluta", ascending=False)
    
    # Mostrar gráfico si se solicita
    if mostrar_grafico:
        plt.figure(figsize=(12,6))
        sns.violinplot(x=col, y=target, data=df, palette="pastel", cut=0)
        plt.title(f"Distribución de {target} según {col}", fontsize=14, fontweight="bold")
        plt.xticks(rotation=45)
        plt.grid(axis="y", linestyle="--", alpha=0.6)
        plt.show()
    
    return resumen


def graficos_numericos(df, col, target):
    """Genera histograma con KDE y boxplot para columnas numéricas"""
    mean_val = df[col].mean()
    median_val = df[col].median()
    
    fig, axes = plt.subplots(1, 2, figsize=(12,5))
    
    # Histograma
    sns.histplot(df[col].dropna(), kde=True, bins=30,
                 color="skyblue", edgecolor="black", alpha=0.7, ax=axes[0])
    axes[0].axvline(mean_val, color="red", linestyle="--", label=f"Media: {mean_val:.2f}")
    axes[0].axvline(median_val, color="green", linestyle="-.", label=f"Mediana: {median_val:.2f}")
    axes[0].set_title(f"Histograma de {col}")
    axes[0].legend()
    axes[0].grid(axis="y", linestyle="--", alpha=0.6)

    
     # Boxplot
    sns.boxplot(x=df[col].dropna(), color="lightgreen", ax=axes[1])
    axes[1].set_title(f"Boxplot de {col}")

    plt.suptitle(f"Distribución de {col}", fontsize=14, fontweight="bold")
    plt.show()

def analizar_target_con_columna_numerica(df, columna, target_column = "precio" ):
  if (df[columna].dtype.kind in ("i","f")) and (columna!=target_column):
    plt.figure(figsize=(14, 5))  # tamaño de la figura
    sns.scatterplot(
    x=columna,
    y=target_column,
    data=df,
    hue=target_column,        # color según precio
    size=target_column,       # tamaño según precio
    alpha=0.7,           # transparencia para mejor visualización
    edgecolor="k"        # borde negro en los puntos
    )

    # Títulos y etiquetas
    plt.title(f"Relación entre {columna} y {target_column}", fontsize=16, fontweight="bold")
    plt.xlabel(columna, fontsize=14)
    plt.ylabel(f"{target_column} (€)", fontsize=14)

    # Ajustar leyenda y diseño
    plt.legend(title=target_column, loc="upper right")
    plt.tight_layout()

def analisis_exploratorio_basico(dataframe):
  for i in dataframe:
    if dataframe[i].dtype.kind == "O":
      #print(i,'\n', dataframe[i].value_counts(dropna=False), '\n')
      print(i,'\n')      
      display(dataframe[i].value_counts(dropna=False))
    elif (dataframe[i].dtype.kind=="f") or (dataframe[i].dtype.kind=="i"):
      print(dataframe.hist(i))

def analisis_exploratorio(df, columnas=None, target="", 
                              display_categoricas = False,
                              display_numericas = False):
    """Análisis exploratorio de un DataFrame"""
    print("📊 Información general del DataFrame")
    print("-"*50)
    print(f"Shape: {df.shape}")
    print("\nTipos de datos:")
    print(df.dtypes)
    print("\nValores nulos por columna:")
    print(df.isnull().sum())
    print("-"*50)
    
    # Selección de columnas
    if columnas is None:
        columnas = df.columns
    
    for col in columnas:
        print(f"\n🔎 Columna: {col}")
        print("-"*30)
        
        # Categóricas
        if (df[col].dtype == "object" or str(df[col].dtype) == "category") and display_categoricas == True:
            print("Tipo: Categórica")
            print(f"Nº de categorías únicas: {df[col].nunique()}")
            print(f"Moda: {df[col].mode()[0] if not df[col].mode().empty else 'N/A'}")
            
            resumen = resumen_categorico(df, col, target)
            display(resumen)
            
            # Gráfico de barras
            plt.figure(figsize=(6,4))
            sns.countplot(x=col, data=df, order=resumen.index)
            plt.title(f"Distribución de {col}")
            plt.xticks(rotation=45)
            plt.show()
        
        # Numéricas
        elif pd.api.types.is_numeric_dtype(df[col]) and display_numericas == True:
            print("Tipo: Numérica")
            print("\nEstadísticas descriptivas:")
            print(df[col].describe())
            
            graficos_numericos(df, col, target)
            analizar_target_con_columna_numerica(df, col, target)
        
        else:
            print("Tipo desconocido")
        
        print("\n")
