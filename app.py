{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "f1924181",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app '__main__'\n",
      " * Debug mode: off\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.\n",
      " * Running on http://127.0.0.1:5000\n",
      "Press CTRL+C to quit\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import gunicorn\n",
    "import pymysql as py\n",
    "from flask import Flask, request, render_template, redirect, url_for, flash, jsonify\n",
    "\n",
    "\n",
    "app = Flask(__name__)\n",
    "\n",
    "@app.route('/')\n",
    "def home():\n",
    "    return 'Flask esta rodando'\n",
    "\n",
    "app.run()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
