# Data Cleaning

Project by Anne Ensign

## About

**Scenario:**

You are a Data Analyst who is working for a company that collects data from veterinary offices in the region. Since most vets are small practices and independently run, you never know what data will come back to you. 

How would you handle a .txt file that came to you like this?

```
Pet name;; owner name;; pet type;; pet dob // Fluffy;; Michael Scott;; cat;; 5/20/2019 // Spots McGoo  ;; Jan  Levinson ;; dog;; 12/1/2015 // Speedy   ;; Ryan Howard ;; turtle ;; unknown // Gordon Gekko ;; Ryan Howard ;; turtle ;; unknown // Winston Churchill ;;   Pam   Beesley ;; dog  ;; 3/30/2009 // Mr. Whiskers  ;; Jim Halpert;; cat ;; 4/5/2018 // Henrietta;; Dwight   Shrute;; porcupine  ;; unknown // Sprinkles ;; Angela Martin  ;; cat ;; 7/19/2000 // Princess Lady;; Angela Martin  ;; cat ;; 8/4/2017 //  Ember ;; Angela Martin  ;; cat ;; 4/3/2015 //   Milky Way ;; Angela Martin  ;; cat ;; 11/15/2012 // Diane;; Angela Martin ;; cat   ;; 9/21/2015 // Lumpy  ;;  Angela  Martin  ;; cat ;; 02/07/2012 // Petals ;; Angela Martin  ;; cat ;; 10/31/2010 // Mr. Ash ;; Angela Martin ;; cat ;; 6/1/2005 // Phillip ;;   Angela Martin;; cat ;; 3/20/2009 // Bandit ;; Angela Martin ;; cat ;; 2/13/2016 // Comstock   ;; Angela Martin ;; cat ;; 10/03/2017 // Lily ;; Stanley Hudson ;; dog ;; 8/8/2012 // Ruth Bader Ginsberg ;; Oscar Martinez ;; dog ;; 9/1/2016 // Neitzsche ;; Oscar Martinez ;; dog ;; 7/31/2015 // Buster ;; Phyllis Vance ;; dog ;; 8/15/2010 // Sadie ;; Meredith Palmer ;; cat ;; 1/15/2020 // Wuphf ;; Kelly Kapoor   ;; dog  ;; 12/3/2018

```

This project is an exercise in cleaning data. I was able to clean it in three different ways:
* Python
* Pandas
* SQLite3

I quickly made a bad .txt file (above) with extra spaces and no commas to practice with. The whole file is on one line. 

Each cleaning method is in a separate Jupyter Notebook.

## Running the Program

It is easiest to have Anaconda (or Miniconda) installed. It has all the packages needed to run the files. [Click here for Anaconda or Miniconda](https://docs.anaconda.com/anaconda/install/index.html). 
If you do not wish to install Anaconda, be sure your machine has the following:
* [Python 3.0 or higher](https://www.python.org)
* [Jupyter Notebook](https://jupyter.org)
* [pandas](https://pandas.pydata.org/pandas-docs/stable/index.html)

Pip install in project folder location or Virtual Environment:
```
pip install notebook
pip install pandas
```

### Running the Program in Jupyter Notebook
1. Clone the repository.
2. Save the folder.
3. Open `jupyter notebook` from the command line or start menu.
4. Navigate to the saved location of the repo.
5. Open `Clean-Up-Pandas.ipynb`, `Clean-Up-Python.ipynb` or `Clean-Up-SQLite.ipynb`.
6. Click `Cell` tab and then `Run All` 