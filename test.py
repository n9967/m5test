{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "9c99eda4",
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'my_sum'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[1], line 3\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01munittest\u001b[39;00m\n\u001b[1;32m----> 3\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01mmy_sum\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;28msum\u001b[39m\n\u001b[0;32m      6\u001b[0m \u001b[38;5;28;01mclass\u001b[39;00m \u001b[38;5;21;01mTestSum\u001b[39;00m(unittest\u001b[38;5;241m.\u001b[39mTestCase):\n\u001b[0;32m      7\u001b[0m     \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21mtest_list_int\u001b[39m(\u001b[38;5;28mself\u001b[39m):\n",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'my_sum'"
     ]
    }
   ],
   "source": [
    "import unittest\n",
    "\n",
    "from my_sum import sum\n",
    "\n",
    "\n",
    "class TestSum(unittest.TestCase):\n",
    "    def test_list_int(self):\n",
    "        \"\"\"\n",
    "        Test that it can sum a list of integers\n",
    "        \"\"\"\n",
    "        data = [1, 2, 3]\n",
    "        result = sum(data)\n",
    "        self.assertEqual(result, 6)\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    unittest.main()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "159db378",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "E\n",
      "======================================================================\n",
      "ERROR: C:\\Users\\n9967\\AppData\\Roaming\\jupyter\\runtime\\kernel-da61fc68-dd73-4140-8ec5-f06708f8fec6 (unittest.loader._FailedTest.C:\\Users\\n9967\\AppData\\Roaming\\jupyter\\runtime\\kernel-da61fc68-dd73-4140-8ec5-f06708f8fec6)\n",
      "----------------------------------------------------------------------\n",
      "AttributeError: module '__main__' has no attribute 'C:\\Users\\n9967\\AppData\\Roaming\\jupyter\\runtime\\kernel-da61fc68-dd73-4140-8ec5-f06708f8fec6'\n",
      "\n",
      "----------------------------------------------------------------------\n",
      "Ran 1 test in 0.001s\n",
      "\n",
      "FAILED (errors=1)\n"
     ]
    },
    {
     "ename": "SystemExit",
     "evalue": "True",
     "output_type": "error",
     "traceback": [
      "An exception has occurred, use %tb to see the full traceback.\n",
      "\u001b[1;31mSystemExit\u001b[0m\u001b[1;31m:\u001b[0m True\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\n9967\\anaconda3\\Lib\\site-packages\\IPython\\core\\interactiveshell.py:3513: UserWarning: To exit: use 'exit', 'quit', or Ctrl-D.\n",
      "  warn(\"To exit: use 'exit', 'quit', or Ctrl-D.\", stacklevel=1)\n"
     ]
    }
   ],
   "source": [
    "if __name__ == '__main__':\n",
    "    unittest.main()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "f5753822",
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'my_sum'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[3], line 4\u001b[0m\n\u001b[0;32m      2\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01munittest\u001b[39;00m\n\u001b[0;32m      3\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01mfractions\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m Fraction\n\u001b[1;32m----> 4\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01mmy_sum\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;28msum\u001b[39m\n\u001b[0;32m      6\u001b[0m \u001b[38;5;28;01mclass\u001b[39;00m \u001b[38;5;21;01mTestSum\u001b[39;00m(unittest\u001b[38;5;241m.\u001b[39mTestCase):\n\u001b[0;32m      7\u001b[0m     \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21mtest_list_int\u001b[39m(\u001b[38;5;28mself\u001b[39m):\n",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'my_sum'"
     ]
    }
   ],
   "source": [
    "# test.py\n",
    "import unittest\n",
    "from fractions import Fraction\n",
    "from my_sum import sum\n",
    "\n",
    "class TestSum(unittest.TestCase):\n",
    "    def test_list_int(self):\n",
    "        \"\"\"\n",
    "        Test that it can sum a list of integers\n",
    "        \"\"\"\n",
    "        data = [1, 2, 3]\n",
    "        result = sum(data)\n",
    "        self.assertEqual(result, 6)\n",
    "\n",
    "    def test_list_fraction(self):\n",
    "        \"\"\"\n",
    "        Test that it can sum a list of fractions\n",
    "        \"\"\"\n",
    "        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]\n",
    "        result = sum(data)\n",
    "        self.assertEqual(result, 1)\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    unittest.main()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8d246677",
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
