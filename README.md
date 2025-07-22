# ⚡ Electricity Consumption Dashboard: Abu Dhabi (2012–2018)

An interactive data science project analyzing electricity consumption by **area** and **sector** in Abu Dhabi between 2012 and 2018.

---

## 📊 Overview

This project explores historical electricity usage patterns across various sectors such as **Residential**, **Commercial**, **Industrial**, **Governmental**, and **Other**. It includes:

- An interactive **Streamlit dashboard**  
- An exploratory **Jupyter Notebook** with visualizations and insights

---

## 🗂 Dataset

**Name:** Electricity consumption by area-sector (2012–2018)  
**Format:** CSV  
**Fields:**

- `year`  
- `Area`  
- `Sector`  
- `UNIT` (Always in GWh)  
- `Consumption`

---

## 🚀 Streamlit Dashboard

### Features

- Interactive filters by **year**, **area**, and **sector**  
- **Trend analysis** with line plots  
- **Sector share breakdown** with stacked area chart  
- **Area comparison** using grouped bar charts  
- **KPIs** showing max/min consumption and YoY changes  
- **Interactive table** with sortable insights

### How to Run Locally

```bash
pip install streamlit pandas plotly
streamlit run app.py
```

### Or View Online

[🔗 View on Hugging Face Spaces](https://huggingface.co/spaces/abdulkarim-suleiman/electricity-consumption-dashboard)

---

## 📓 Jupyter Notebook: EDA & Visualization

Includes:

- Yearly consumption trends  
- Sector-wise comparisons  
- Area-sector heatmaps  
- Key statistical summaries

### How to Run

```bash
pip install pandas matplotlib seaborn plotly
jupyter notebook electricity_eda_notebook.ipynb
```

---

## 📁 Files

- `app.py` – Streamlit dashboard code  
- `electricity_eda_notebook.ipynb` – Jupyter Notebook for EDA  
- `electricity_consumption_by_area-sector_2012-2018.csv` – Raw dataset  
- `README.md` – Project documentation

---

## 🧰 Tech Stack

- **Python**  
- **Pandas** & **Seaborn**  
- **Plotly**  
- **Streamlit**

---

## 👨‍💻 Author

Made by a Data Science Enthusiast passionate about energy, sustainability, and storytelling with data.

Connect on [LinkedIn](https://linkedin.com/in/abdulkarim-suleiman-a6956014b)

---

## 🙌 Contributions & Feedback

Feel free to fork, comment, or reach out with suggestions!
