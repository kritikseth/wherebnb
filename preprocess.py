import folium
from folium import plugins
import mapping as mp
import numpy as np

def make_map(df, CityId):

    City = mp.id_city_dict[CityId]

    dfs = df[df['city']==City].drop(['city'], axis=1)
    # if dfs.shape[0]>=1500:
    #     dfs = dfs.sample(n=1500)
    dfs = dfs.values.tolist()

    map = folium.Map(mp.city_latlong_dict[CityId], zoom_start=12,
                    width='100%',
                    height='100%')
    clusts = plugins.MarkerCluster().add_to(map)

    for l, l1, l2, t, pr, r, po in dfs:
        pop_up = f'{l} || Type: {t} ||  Reviews: {r} || Popularity: {po} || Price: ${pr}/night'
        if t=='Entire Home':
            folium.Marker([l1, l2], 
                        icon=folium.Icon(color='black',icon='home', prefix='fa'),
                        popup=pop_up).add_to(clusts)
        if t=='Hotel Room':
            folium.Marker([l1, l2], 
                        icon=folium.Icon(color='black',icon='bed', prefix='fa'),
                        popup=pop_up).add_to(clusts)
        if t=='Private Room':
            folium.Marker([l1, l2], 
                        icon=folium.Icon(color='black',icon='user', prefix='fa'),
                        popup=pop_up).add_to(clusts)
        if t=='Shared Room':
            folium.Marker([l1, l2], 
                        icon=folium.Icon(color='black',icon='users', prefix='fa'),
                        popup=pop_up).add_to(clusts)

    return map


def classifier(form_data, clf):
    
    test = [int(form_data['room_type'][0]), float(form_data['price']), float(form_data['minimum_nights']),
            float(form_data['number_of_reviews']), float(form_data['reviews_per_month']),
            float(form_data['calculated_host_listings_count']), float(form_data['availability_365']),
            int(form_data['city'][0])]

    return mp.id_pop_dict[list(clf.predict([test]))[0]]


# def regressor(form_data, CityId, reg):
    
#     test = [mp.hood_latlong_dict[CityId][0], mp.hood_latlong_dict[CityId][1], mp.hood_latlong_dict[CityId][2],
#             int(form_data['room_type']), np.log1p(float(form_data['minimum_nights'])), float(form_data['number_of_reviews']),
#             np.sqrt(float(form_data['reviews_per_month'])), float(form_data['calculated_host_listings_count']),
#             float(form_data['availability_365']), int(form_data['city']), float(form_data['popularity'])]

#     return int(round(np.expm1(list(reg.predict([test]))[0]), 0))


def regressor(form_data, CityId, reg):
    
    test = [int(form_data['room_type']), float(form_data['minimum_nights']), float(form_data['number_of_reviews']),
            float(form_data['reviews_per_month']), float(form_data['calculated_host_listings_count']),
            float(form_data['availability_365']), int(form_data['city']), float(form_data['popularity'])]

    return int(round(list(reg.predict([test]))[0]))