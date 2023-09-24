from flask import Flask,render_template,send_from_directory

import os
from Utils.paths import get_base_path
from mainloop import main_loop
output_folder = 'Outputs'
datasets_folder = 'Datasets'

dataset_file_name = "restaurant_data.json"
csv_file_name_1 = "restaurant_data.csv"
csv_file_name_2 = "restaurant_events.csv"
dataset_file_path = os.path.join(get_base_path(__file__),datasets_folder, dataset_file_name)
csv_file_path_1 = os.path.join(get_base_path(__file__), output_folder, csv_file_name_1)
csv_file_path_2 = os.path.join(get_base_path(__file__), output_folder, csv_file_name_2)

app = Flask(__name__,template_folder='html')

@app.route('/')
def run_main_loop():
    averages=main_loop(dataset_file_path,csv_file_path_1,csv_file_path_2)
    excellent_avg= averages.get('excellent',0)
    very_good_avg= averages.get('very_good',0)
    good_avg = averages.get('good',0)
    average_avg = averages.get('average',0)
    poor_avg = averages.get('poor',0)
    return render_template('index.html',excellent_avg=excellent_avg,very_good_avg=very_good_avg,good_avg=good_avg,average_avg=average_avg,poor_avg=poor_avg)
@app.route('/download/<filename>')
def download_csv(filename):
    # Ensure that the requested file exists in the 'Outputs' folder
    file_path = os.path.join(output_folder, filename)
    if os.path.isfile(file_path):
        return send_from_directory(output_folder, filename, as_attachment=True)
    else:
        return 'File not found, error code:', 404

if __name__ == '__main__':
    app.run(debug=True)
