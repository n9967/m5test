{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "ad9ffc79",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "E\n",
      "======================================================================\n",
      "ERROR: C:\\Users\\n9967\\AppData\\Roaming\\jupyter\\runtime\\kernel-b6760a10-f906-4345-b4d3-81d68a23b372 (unittest.loader._FailedTest.C:\\Users\\n9967\\AppData\\Roaming\\jupyter\\runtime\\kernel-b6760a10-f906-4345-b4d3-81d68a23b372)\n",
      "----------------------------------------------------------------------\n",
      "AttributeError: module '__main__' has no attribute 'C:\\Users\\n9967\\AppData\\Roaming\\jupyter\\runtime\\kernel-b6760a10-f906-4345-b4d3-81d68a23b372'\n",
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
    "import unittest\n",
    "\n",
    "\n",
    "class TestSum(unittest.TestCase):\n",
    "\n",
    "    def test_sum(self):\n",
    "        self.assertEqual(sum([1, 2, 3]), 6, \"Should be 6\")\n",
    "\n",
    "    def test_sum_tuple(self):\n",
    "        self.assertEqual(sum((1, 2, 2)), 6, \"Should be 6\")\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    unittest.main()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f02a1317",
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
