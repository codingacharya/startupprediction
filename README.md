git clone https://github.com/codingacharya/startupprediction.git

cd startupprediction

python -m venv venv

venv\Scripts\activate 

pip install -r r.txt

jupyter notebook notebooks/training.ipynb

streamlit run app.py
