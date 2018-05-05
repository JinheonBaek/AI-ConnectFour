# AI - Connect Four

## Korea Univ. AI Class (COSE-361, Section Num 2, Spring, 2018)

Connect four AI Model, </br>
Made by 라건우(Geonu La) / 백진헌(Jinheon Baek) / 태영준(Yeongjun Tae)

## Prerequisites
* Python (>= 3.6)
* pandas
* pickle
* Maybe more, just use pip install if you get an error.

## Our Approach
1. Rule Base
2. Heuristic (Minmax, Alpha-Beta Pruning)
3. NN_Heuristic (Minmax, Alpha-Beta Pruning using Neural Network)

## Files
* main.py </br>
Main Function to run Connect four Game

* board.py </br>
Connect four board Class

* rule.py </br>
Rule Class for Rule base approach

* heuristic.py </br>
Connect four Heuristic Class </br>
Heuristic Class: Simple Heuristic </br>
NN_Heuristic Class: Mixed way Heuristic (Our Thinking + NN Model)

* Data Folder </br>
Connect four dataset (UCI Dataset)

* Model Folder </br>
Connect four Machine Learning Model </br>
MLP : Neural Network (MLP) </br>
SVM : Support Vector Machine

* Learning (learning.ipynb) </br>
File for Connect four Machine Learning(NN / SVM) based on the jupyter notebook