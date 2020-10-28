<a href="https://wherebnb.herokuapp.com/" target="_blank"><h1 style="color:#0056B3">wherebnb.</h1></a>
<h3>made by- Kritik Seth</h3>

Wherebnb is an application that uses machine learning in the backend and provides:

* Tourists with price estimates of a house in any region, based on features they have selected.
* Hosts with popularity estimates of their house if they were to put it up for rent on Airbnb, it also suggests pricing for that house.
* Users with a map of nearby places actually available for rent on Airbnb in the selected region.
* Travellers with a list of nearby experiences in the selected city.

<!-- This repository contains only the backend functions of [wherebnb.](https://wherebnb.herokuapp.com/) web application. Many of the files have been hidden in order to make this difficult to reproduce without my consent.
If you want to have a look at all the files, contact me. -->

#### Installation of wherebnb.

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

#### Directory
```
├── app.py
├── mapping.py
├── preprocess.py
├── templates 
│   ├── about.html
│   ├── base.html
│   ├── child.html
│   ├── data.html
│   ├── host.html
│   ├── index.html
│   ├── map.html
│   ├── nearby.html
│   ├── mapnearbyview.html
│   ├── mapview.html
│   ├── nearby.html
│   ├── nearbyview.html
│   ├── popularity.html
│   ├── popularityresult.html
│   ├── price.html
│   ├── priceresult.html
│   └── tourist.html
├── static
│   ├── css
│   │   ├── neumorphism.css
│   │   └── neumorphism.css.map
│   ├── data
│   │   ├── wherebnb-map-1000.csv
│   │   └── wherebnb-map-2000.csv
│   ├── img
│   │   ├── brand
│   │   │   ├── ...
│   │   ├── loading
│   │   │   ├── ...
│   │   └── profile
│   │   │   ├── ...
│   ├── js
│   │   ├── neumorphism.js
│   ├── models
│   │   ├── [generated maps]
│   ├── models
│   │   ├── decision_tree_clf.pkl
│   │   ├── lgbm.pkl
│   │   └── lgbm_all.pkl
│   ├── scss
│   │   ├── bootstrap
│   │   │   ├── ...
│   │   ├── neumorphism
│   │   │   ├── ...
│   │   └── neumorphism.scss
│   └── vendor
│   │   ├── ...
├── processing
│   ├── __init__.py
├── requirements.txt
├── LICENSE
├── Procfile
└── README.md
```

This dataset can also be found on **kaggle** here- [U.S. Airbnb Open Data](https://www.kaggle.com/kritikseth/us-airbnb-open-data)

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

