import json
from datetime import datetime
import csv
from Utils.extractors import extract_data,extract_event_data,extract_user_rating

def main_loop(dataset_file_path,csv_file_path_1,csv_file_path_2):
    ## load file
    with open(dataset_file_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    ## qn 1 write to csv file
    fields_to_extract = ["Restaurant ID", "Restaurant Name", "Country", "City", "User Rating Votes", "User Aggregate Rating", "Cuisines"]
    with open(csv_file_path_1, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.DictWriter(csvfile, fieldnames=fields_to_extract)
        csv_writer.writeheader()
        ## O(n^2) complexity
        for index in data:
            for restaurant in index['restaurants']:  # Access the 'restaurants' array within the JSON
                extracted_data = extract_data(restaurant)
                csv_writer.writerow(dict(zip(fields_to_extract, extracted_data)))
    ## qn 2 write to csv file
    next_fields_to_extract = ["Event ID","Restaurant ID", "Restaurant Name","Photos Url","Title","Start Date", "End Date"]
    with open(csv_file_path_2, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.DictWriter(csvfile, fieldnames=next_fields_to_extract)
        csv_writer.writeheader()
        ## O(n^2) complexity
        for index in data:
            for restaurant in index['restaurants']:  # Access the 'restaurants' array within the JSON
                
                extracted_event_data = extract_event_data(restaurant)
    
                if(len(extracted_event_data[3]) ==0):
                    csv_writer.writerow(dict(zip(next_fields_to_extract, ["NA",extracted_event_data[0],extracted_event_data[1],"NA","NA","NA","NA"])))
                else:
                    count = 0
           
                    for event_data in extracted_event_data[3]:
                        
                        date_object = datetime.strptime(event_data['event']['start_date'], "%Y-%m-%d")

                        if(date_object.year == 2019 and date_object.month==4):
                            csv_writer.writerow(dict(zip(next_fields_to_extract, [event_data['event']['event_id'],extracted_event_data[0],extracted_event_data[1],extracted_event_data[2],event_data['event']['title'],event_data['event']['start_date'],event_data['event']['end_date']])))
                            count = count + 1
                    
                    if(count == 0):
                        csv_writer.writerow(dict(zip(next_fields_to_extract, ["NA",extracted_event_data[0],extracted_event_data[1],"NA","NA","NA","NA"])))
    ## qn 3 "user_rating": {"aggregate_rating": "4.6", "rating_text": "Excellent", "rating_color": "3F7E00", "votes": "13627", "has_fake_reviews": 0}
    excellent=[]
    very_good=[]
    good=[]
    average=[]
    poor=[]
    for index in data:
        for restaurant in index['restaurants']:
            extracted_user_data= extract_user_rating(restaurant)
            if(extracted_user_data['rating_text']=="Excellent"):
                excellent.append(float(extracted_user_data['aggregate_rating']))
            elif(extracted_user_data['rating_text']=="Very Good"):
                very_good.append(float(extracted_user_data['aggregate_rating']))
            elif(extracted_user_data['rating_text']=="Good"):
                good.append(float(extracted_user_data['aggregate_rating']))
            elif(extracted_user_data['rating_text']=="Average"):
                average.append(float(extracted_user_data['aggregate_rating']))
            elif(extracted_user_data['rating_text']=="Poor"):
                poor.append(float(extracted_user_data['aggregate_rating']))
    excellent_avg= sum(excellent)/len(excellent)
    very_good_avg= sum(very_good)/len(very_good)
    good_avg= sum(good)/len(good)
    average_avg= sum(average)/len(average)
    poor_avg= sum(poor)/len(poor)

    return {'excellent':excellent_avg,'very_good':very_good_avg,'good':good_avg,'average':average_avg,'poor':poor_avg}