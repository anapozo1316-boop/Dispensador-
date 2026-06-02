# SURGIWRAP

## Dispensador Inteligente de Tela para Instrumental Quirúrgico

### Descripción

SURGIWRAP es un prototipo de software desarrollado en Streamlit para controlar una máquina dispensadora y cortadora de tela utilizada en el envoltorio de instrumental quirúrgico.

La aplicación permite:

- Configurar la longitud de tela.
- Configurar la cantidad de cortes.
- Simular el proceso de corte.
- Ajustar la velocidad de operación.
- Visualizar el estado general del sistema.

### Tecnologías utilizadas

- Python
- Streamlit

### Estructura del proyecto

```
SurgiWrap/
│
├── app.py
├── requirements.txt
└── README.md
```

### Instalación

1. Clonar el repositorio:

```bash
git clone URL_DEL_REPOSITORIO
```

2. Instalar dependencias:

```bash
pip install -r requirements.txt
```

3. Ejecutar la aplicación:

```bash
streamlit run app.py
```

### Funcionalidades

#### Inicio
Visualiza el estado actual de la máquina.

#### Longitud
Permite configurar la longitud de tela a cortar.

#### Cantidad
Permite definir la cantidad de cortes.

#### Corte
Simula el proceso de corte mediante una barra de progreso.

#### Ajustes
Permite seleccionar la velocidad de operación.

### Autor

Ana Pozo

### Proyecto Académico

Desarrollo de un prototipo de interfaz para una máquina dispensadora inteligente de tela destinada al envoltorio de instrumental quirúrgico.
