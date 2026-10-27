# Data Source

**Dataset:** Pima Indians Diabetes Database
**Original source:** National Institute of Diabetes and Digestive and Kidney Diseases (NIDDK), USA
**Mirror used:** https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.csv
(a widely-used, stable public mirror of the classic UCI/Kaggle "Pima Indians Diabetes" dataset —
the original UCI page: https://archive.ics.uci.edu/dataset/34/diabetes ,
also hosted on Kaggle: https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database)
**Retrieved:** 2026-09-18
**License:** Public domain / CC0 (per UCI Machine Learning Repository terms)
**Rows x Columns (raw):** 768 x 9
**File:** diabetes.csv (no header row in the raw file — column names are applied in `src/load_data.py`)
**Note:** File shows 767 lines because it has no trailing newline after the 768th record; `wc -l`
undercounts by one when the last line is unterminated. Verified 768 records on load.
