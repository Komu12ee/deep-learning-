{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "65af4d2f",
   "metadata": {},
   "outputs": [
    {
     "ename": "",
     "evalue": "",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31mRunning cells with '.conda (Python 3.11.14)' requires the ipykernel package.\n",
      "\u001b[1;31mInstall 'ipykernel' into the Python environment. \n",
      "\u001b[1;31mCommand: 'conda install -n .conda ipykernel --update-deps --force-reinstall'"
     ]
    }
   ],
   "source": [
    "import numpy as np \n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f33dd382",
   "metadata": {},
   "outputs": [],
   "source": [
    "df=pd.read_csv('placement.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1a20ee6d",
   "metadata": {},
   "outputs": [],
   "source": [
    "print(df.head())\n",
    "print(df.shape)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "eea364c8",
   "metadata": {},
   "outputs": [],
   "source": [
    "sns.scatterplot(x='cgpa', y='resume_score', hue='placed', data=df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b2cb1fe6",
   "metadata": {},
   "outputs": [],
   "source": [
    "x=df.iloc[:,0:2]\n",
    "y=df.iloc[:,-1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "74ea1875",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.linear_model import Perceptron\n",
    "p = Perceptron()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5a35f03d",
   "metadata": {},
   "outputs": [],
   "source": [
    "p.fit(x,y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "56bf1f4a",
   "metadata": {},
   "outputs": [],
   "source": [
    "p.coef_"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8aca234c",
   "metadata": {},
   "outputs": [],
   "source": [
    "from mlxtend.plotting import plot_decision_regions"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b2c307f9",
   "metadata": {},
   "outputs": [],
   "source": [
    "plot_decision_regions(x.values,y.values,clf=p,legend=2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a3e18e9b",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "traffic",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "name": "python",
   "version": "3.11.14"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
