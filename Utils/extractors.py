country_code_to_name = {
    1: 'India',
    14: 'Australia',
    30: 'Brazil',
    37: 'Canada',
    94: 'Indonesia',
    148: 'New Zealand',
    162: 'Phillipines',
    166: 'Qatar',
    184: 'Singapore',
    189: 'South Africa',
    191: 'Sri Lanka',
    208: 'Turkey',
    214: 'UAE',
    215: 'United Kingdom',
    216: 'United States'
}

def extract_data(restaurant):
    restaurant_info = restaurant['restaurant']  # Access the 'restaurant' object
    restaurant_id = restaurant_info['R']['res_id']  # Access the 'res_id' within 'R'
    name = restaurant_info['name']
    country_code = restaurant_info['location']['country_id']  # Access 'country_id' within 'location'
    country = country_code_to_name.get(country_code)
    city = restaurant_info['location']['city']
    user_rating_votes = restaurant_info['user_rating']['votes']  # Access 'votes' within 'user_rating'
    user_aggregate_rating = restaurant_info['user_rating']['aggregate_rating']
    cuisines = restaurant_info['cuisines']
    return [restaurant_id, name, country, city, user_rating_votes, user_aggregate_rating, cuisines]

def extract_event_data (restaurant):
    restaurant_info = restaurant['restaurant']  # Access the 'restaurant' object
    name = restaurant_info['name']
    restaurant_id = restaurant_info['R']['res_id']  # Access the 'res_id' within 'R'
    events = restaurant_info.get('zomato_events', []) 
    photos_url = restaurant_info.get('photos_url', 'NA') 
            
    return [restaurant_id, name,photos_url,events]
def extract_user_rating (restaurant):
    restaurant_info = restaurant['restaurant']  # Access the 'restaurant' object
    user_rating = restaurant_info.get('user_rating', {})
    return user_rating