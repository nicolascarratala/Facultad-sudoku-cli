FROM python

WORKDIR usr/src/sudoku

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

CMD ["python","Run.py"]