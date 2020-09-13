# Result Notifier Bachelor's Side Project
## Web Scraping
## Python


I have used a different library to implement result notifier algorithm. So, Use the package manager [pip](https://pip.pypa.io/en/stable/) to install a dependency.

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

This program scraps GTU result website and fetches all the declared results. After getting the results, it compares with specific keyword and if the new result is declared then it directly sends SMS and an email notification to every registered student.
