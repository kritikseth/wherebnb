<a href="https://wherebnb.herokuapp.com/" target="_blank"><h1 style="color:#0056B3">wherebnb.</h1></a>
<h3>made by- Kritik Seth</h3>

Wherebnb is an application that uses machine learning in the backend and provides:

* Tourists with price estimates of a house in any region, based on features they have selected.
* Hosts with popularity estimates of their house if they were to put it up for rent on Airbnb, it also suggests pricing for that house.
* Users with a map of nearby places actually available for rent on Airbnb in the selected region.
* Travellers with a list of nearby experiences in the selected city.

#### Website Link- https://wherebnb.herokuapp.com/
<!-- This repository contains only the backend functions of [wherebnb.](https://wherebnb.herokuapp.com/) web application. Many of the files have been hidden in order to make this difficult to reproduce without my consent.
If you want to have a look at all the files, contact me. -->

### Installation of wherebnb.

1. In your command prompt or terminal run
```
git clone https://github.com/kritikseth/wherebnb.git
```

2. Install requirements
```
pip3 install -r requirements.txt --user
```
3. Run the application
```
python3 app.py
```

### Directory
```
├── Data
│   └── ...
├── LICENSE
├── Procfile
├── README.md
├── app.py
├── hosted
│   └── ...
├── mapping.py
├── preprocess.py
├── requirements.txt
├── static
│   ├── css
│   │   ├── neumorphism.css
│   │   └── neumorphism.css.map
│   ├── data
│   │   ├── wherebnb-map-1000.csv
│   │   └── wherebnb-map-2000.csv
│   ├── img
│   │   ├── brand
│   │   ├── loading
│   │   └── profile
│   ├── js
│   │   └── neumorphism.js
│   ├── maps
│       └── [generated maps]
│   ├── models
│   │   ├── decision_tree_clf.pkl
│   │   ├── lgbm.pkl
│   │   └── lgbm_all.pkl
│   ├── scss
│   │   ├── bootstrap
│   │   ├── neumorphism
│   │   └── neumorphism.scss
│   └── vendor
│       └── ...
└── templates
    ├── about.html
    ├── base.html
    ├── child.html
    ├── data.html
    ├── host.html
    ├── index.html
    ├── map.html
    ├── mapnearby.html
    ├── mapnearbyview.html
    ├── mapview.html
    ├── nearby.html
    ├── nearbyview.html
    ├── popularity.html
    ├── popularityresult.html
    ├── price.html
    ├── priceresult.html
    └── tourist.html

```

### Technologies Used

![](https://forthebadge.com/images/badges/made-with-python.svg)

[<img target="_blank" src="https://upload.wikimedia.org/wikipedia/commons/0/05/Scikit_learn_logo_small.svg" width=150>](https://scikit-learn.org/stable/) [<img target="_blank" src="https://flask.palletsprojects.com/en/1.1.x/_images/flask-logo.png" width=180>](https://flask.palletsprojects.com/en/1.1.x/) [<img target="_blank" src="https://number1.co.za/wp-content/uploads/2017/10/gunicorn_logo-300x85.png" width=180>](https://gunicorn.org)

[<img target="_blank" src="https://lightgbm.readthedocs.io/en/latest/_images/LightGBM_logo_black_text.svg" width=180>](https://lightgbm.readthedocs.io/en/latest/) 
[<img target="_blank" src="https://www.tableau.com/sites/default/files/pages/tableau_cmyk_2015.png" width=200>](https://www.tableau.com/) 

[<img target="_blank" src="https://joblib.readthedocs.io/en/latest/_static/joblib_logo.svg" width=120>](https://joblib.readthedocs.io/en/latest/) [<img target="_blank" src="https://images.g2crowd.com/uploads/product/image/social_landscape/social_landscape_bf0fb4cb7fe948c42f37ded73895638f/salesforce-heroku.png" width=180>](https://www.heroku.com/)[<img target="_blank" src="https://openjsf.org/wp-content/uploads/sites/84/2019/10/jquery-logo-vertical_large_square.png" width=100>](https://jquery.com/)

### Made by
[![Kritik Seth](https://avatars2.githubusercontent.com/u/39276404?s=460&u=fa82c2a3cbf3454758cafdc9e834745f1434b802&v=4)](https://kritikseth.github.io/) |
-|
[Kritik Seth](https://kritikseth.github.io/) |)

### Bug/Feature Request
* If you find a bug (the website couldn't handle the query and/or gave undesired results), kindly open an issue [here](https://github.com/kritikseth/wherebnb/issues/new) by including your search query and the expected result.
* If you'd like to request a new function, feel free to do so by opening an issue [here](https://github.com/kritikseth/wherebnb/issues/new). Please include sample queries and their corresponding results.


### License
[![Apache license](https://img.shields.io/badge/license-apache-blue?style=for-the-badge&logo=appveyor)](https://www.apache.org/licenses/LICENSE-2.0)

Copyright 2020 Kritik Seth

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific la

### Dataset
This dataset can also be found on **kaggle** here- [U.S. Airbnb Open Data](https://www.kaggle.com/kritikseth/us-airbnb-open-data)

### Product Images
**Home Page**

![](https://raw.githubusercontent.com/kritikseth/wherebnb/main/hosted/wherebnb-card-image.png)

**Price Prediction**

![](https://raw.githubusercontent.com/kritikseth/wherebnb/main/hosted/wherebnb_product_display_1.png)

**Popularity Prediction**

![](https://raw.githubusercontent.com/kritikseth/wherebnb/main/hosted/wherebnb_product_display_2.png)

**Map**

![](https://raw.githubusercontent.com/kritikseth/wherebnb/main/hosted/wherebnb_product_display_3.png)

**Nearby Experiences**

![](https://raw.githubusercontent.com/kritikseth/wherebnb/main/hosted/wherebnb_product_display_4.png)

