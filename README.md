# Result Notifier
## Web Scraping
## Python


I have used different library to implement result notifier algorithm. So, Use the package manager [pip](https://pip.pypa.io/en/stable/) to install dependency.

```bash
pip install -r requirements.txt
```

### To run the program.

Open Console

Go to the directory of the program file and then execute below line in the console
```
python Notifier.py
```
You can see an output in the console.

This program scraps GTU result website and fetch all the declared results. After getting the results, it compares with specific keyword and if recently new result is declared then it directly send SMS and email notification to every registered student.
