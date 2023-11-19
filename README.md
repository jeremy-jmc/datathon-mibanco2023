# datathon-mibanco2023

Project folder structure
```
project_name/
│
├── data/
│   ├── raw/                     # Raw data files (original datasets)
│   │   ├── dataset1.csv
│   │   ├── dataset2.xlsx
│   │   └── ...
│   │
│   ├── processed/               # Processed data files (cleaned, transformed data)
│   │   ├── dataset1_cleaned.csv
│   │   ├── dataset2_cleaned.csv
│   │   └── ...
│   │
│   ├── external/                # External data (data from external sources, if any)
│   │   ├── external_data1.csv
│   │   ├── external_data2.json
│   │   └── ...
│   │
│   └── README.md                # Description of the data, data dictionary, source info, etc.
│
├── notebooks/                   # Jupyter notebooks for data exploration, analysis, and visualization
│   ├── exploratory_data_analysis.ipynb
│   ├── data_preprocessing.ipynb
│   ├── model_training.ipynb
│   ├── model_evaluation.ipynb
│   └── ...
│
├── src/                         # Python scripts for data preprocessing and model training
│   ├── data_preprocessing.py
│   ├── model.py
│   └── ...
│
├── models/                      # Saved model files
│   ├── model1.pkl
│   ├── model2.h5
│   └── ...
│
├── results/                     # Results and evaluation metrics
│   ├── evaluation_metrics.txt
│   ├── model_performance_plots/
│   │   ├── confusion_matrix.png
│   │   ├── roc_curve.png
│   │   └── ...
│   └── ...
│
├── config/                      # Configuration files (e.g., hyperparameters)
│   ├── config.yaml
│   ├── hyperparameters.json
│   └── ...
│
├── requirements.txt              # Python package dependencies
├── README.md                    # Project documentation and instructions
└── LICENSE                       # License information for your project
```




# TO DO

- [x] Imputación de variables categoricas en customers dataset.
- [x] Elección de variables simples de balances para el modelo. 
- [x] Probar regresión logistica. 
- [ ] Feature engineering al mango :v

# Variables

## Balances

PERIODO - Periodo de extracción de los datos
ID - Identificador único

CANT_EMP_NEG - Cantidad de empresas de negocio
CANT_EMP_CONS - Cantidad de empresas de consumo
CANT_EMP_HIPOT - Cantidad de empresas hipotecario
    * last
    * variable para ver si cerro o abrio empresas en los ultimos 9 meses

SALDO_MED_EMP - Saldo en mediana empresa
SALDO_PEQ_EMP - Saldo en pequeña empresa
SALDO_MIC_EMP - Saldo en micro empresa
    * categorica para saber que tipo de empresa tiene
    * last
    * variacion promedio de los saldos en los saldos que tiene

SALDO_CONS_REV - Saldo Consumo revolvente
SALDO_CONS_NO_REV - Saldo Consumo NO revolvente
    
SALDO_HIPOT - Saldo en hipotecario
SALDO_VENCIDO - Saldo vencido

CANT_EMP_DOL_NEG - Cantidad de empresas de negocios en dólares
SALDO_DOLA_NEG - Saldo en dólares de negocio
CANT_EMP_DOL_CONS - Cantidad de empresas de consumo en dólares
SALDO_DOLA_CONS - Saldo en dólares de consumo
CANT_EMP_DOL_HIPOT - Cantidad de empresas de hipotecario en dólares
SALDO_DOLA_HIPOT - Saldo en dólares de hipotecario
MAX_LINEA_DISP_U6M - Línea Máxima disponible en los últimos 6 meses
