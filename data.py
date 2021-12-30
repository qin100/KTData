import pandas as pd
import numpy as np
import csv

def n_q_r(filename,features,selected_features,save_name):
    students = {}
    students_list = []
    skills = []
    users_id = []
    features = features


    selected_features = selected_features
    all_data = pd.read_csv(filename, encoding='ISO-8859-1')
    filtered_data = all_data[features]
    filtered_data = filtered_data[filtered_data['ms_first_response'] > 0]
    filtered_data = filtered_data.fillna(-1)

    for index, row in filtered_data.iterrows():
        if row['skill_id'] == -1:
            continue
        if row['skill_id'] not in skills:
            skills.append(int(row['skill_id']))
        if row['user_id'] not in users_id:
            users_id.append(int(row['user_id']))
        if row['user_id'] in students:
            students[row['user_id']].append(row[selected_features].values.tolist())
        else:
            students[row['user_id']] = [row[selected_features].values.tolist()]


    with open(save_name, 'w', newline='') as csvfile:
        for user_id in users_id:
            num = len(students[user_id])
            qau = np.array(students[user_id])
            qau = qau.reshape(-1,3)
            writer = csv.writer(csvfile)

            writer.writerow([num])
            writer.writerow(qau[:,0])
            writer.writerow(qau[:,1])

if __name__ == '__main__':
    features = ['assignment_id', 'assistment_id', 'problem_id', 'user_id', 'original', 'correct', 'attempt_count',
                'ms_first_response',
                'skill_id', 'hint_count', 'first_action', 'bottom_hint']

    selected_features = ['skill_id', 'correct','user_id']

    filename = './data/skill_builder_data_corrected.csv'

    save_name = 'assistment2009-3'

    n_q_r(filename,features,selected_features,save_name)