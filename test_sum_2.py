{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "7461c6b4",
   "metadata": {},
   "outputs": [
    {
     "ename": "AssertionError",
     "evalue": "Should be 6",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mAssertionError\u001b[0m                            Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[1], line 9\u001b[0m\n\u001b[0;32m      7\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;18m__name__\u001b[39m \u001b[38;5;241m==\u001b[39m \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m__main__\u001b[39m\u001b[38;5;124m\"\u001b[39m:\n\u001b[0;32m      8\u001b[0m     test_sum()\n\u001b[1;32m----> 9\u001b[0m     test_sum_tuple()\n\u001b[0;32m     10\u001b[0m     \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mEverything passed\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n",
      "Cell \u001b[1;32mIn[1], line 5\u001b[0m, in \u001b[0;36mtest_sum_tuple\u001b[1;34m()\u001b[0m\n\u001b[0;32m      4\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21mtest_sum_tuple\u001b[39m():\n\u001b[1;32m----> 5\u001b[0m     \u001b[38;5;28;01massert\u001b[39;00m \u001b[38;5;28msum\u001b[39m((\u001b[38;5;241m1\u001b[39m, \u001b[38;5;241m2\u001b[39m, \u001b[38;5;241m2\u001b[39m)) \u001b[38;5;241m==\u001b[39m \u001b[38;5;241m6\u001b[39m, \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mShould be 6\u001b[39m\u001b[38;5;124m\"\u001b[39m\n",
      "\u001b[1;31mAssertionError\u001b[0m: Should be 6"
     ]
    }
   ],
   "source": [
    "def test_sum():\n",
    "    assert sum([1, 2, 3]) == 6, \"Should be 6\"\n",
    "\n",
    "def test_sum_tuple():\n",
    "    assert sum((1, 2, 2)) == 6, \"Should be 6\"\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    test_sum()\n",
    "    test_sum_tuple()\n",
    "    print(\"Everything passed\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d246babb",
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
   "version": "3.11.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
