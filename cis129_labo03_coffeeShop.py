{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 221,
   "id": "3c4befc7-b50e-4dbf-aff2-c43a66b2a7ea",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "***************************************     \n",
      "My Coffee and Muffin Shop\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Number of coffees bought? 1\n",
      "Number of muffins bought? 2\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "***************************************\n",
      "***************************************     \n",
      "My Coffee and Muffin Shop Receipt\n",
      "1 Coffee at $5 each: $ 5.00\n",
      "2 Muffins at $4 each: $ 8.00\n",
      "6% tax: 0.78\n",
      "---------\n",
      "Total: 13.78\n",
      "***************************************\n"
     ]
    }
   ],
   "source": [
    "#cis129_lab03_coffeeShop.py\n",
    "print('***************************************\\\n",
    "     \\nMy Coffee and Muffin Shop')\n",
    "\n",
    "value1 = int(input('Number of coffees bought?')) #Coffee Amount = value1\n",
    "\n",
    "value2 = int(input('Number of muffins bought?')) #Muffin Amount = value2\n",
    "\n",
    "print('***************************************')\n",
    "print('***************************************\\\n",
    "     \\nMy Coffee and Muffin Shop Receipt')\n",
    "\n",
    "#total muffin cost = value3\n",
    "value3 = float(value1 * 5.00)\n",
    "print(value1, 'Coffee at $5 each:', '$', (format(value3, '.2f'))) \n",
    "\n",
    "#total muffin cost = value4\n",
    "value4 = float(value2 * 4.00)\n",
    "print(value2, 'Muffins at $4 each:', '$',(format(value4, '.2f')))\n",
    "\n",
    "#tax total = value5\n",
    "value5 = (value3 + value4) * 0.06\n",
    "print('6% tax:', value5)\n",
    "\n",
    "print('---------')\n",
    "print('Total:', (value3 + value4 + value5))\n",
    "print('***************************************')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "70d71c9f-674c-4641-9960-649152a67dd1",
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.12.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
