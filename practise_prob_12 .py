{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "a1827ee1-669e-4576-a24f-de3831638115",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'set'>\n",
      "{9, '9.0'}\n"
     ]
    }
   ],
   "source": [
    "## WAP to figure out a way to store 9 nad 9.0 as seperate values in a set \n",
    "#(You can take help of built in data types)\n",
    "\n",
    "#there are many possible solutions for this question \n",
    "\n",
    "#1 \n",
    "\n",
    "collection = {9 , \"9.0\"}  #save either one as a string\n",
    "\n",
    "print(type(collection))\n",
    "\n",
    "print(collection)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "0b370fc0-370b-4525-8c21-d473276832d8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'set'>\n",
      "{('float', 9.0), ('int', 9)}\n"
     ]
    }
   ],
   "source": [
    "#2 \n",
    "\n",
    "collection={(\"float\",9.0) , (\"int\",9)}\n",
    "\n",
    "print(type(collection))\n",
    "\n",
    "print(collection)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
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
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
