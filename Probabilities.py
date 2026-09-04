from collections import Counter
#import matplotlib.pyplot as plt

# Example: Predicting daily activities (represented as numbers)
# 0=Sleep, 1=Work, 2=Exercise, 3=Social, 4=Leisure

historical_activities = [0, 1, 2, 1, 3, 1, 4, 0, 1, 2, 1, 3, 1, 4, 0]

def calculate_probabilities(sequence):
    count = Counter(sequence)
    length = len(sequence)
    probability = {activity: count / length for activity, count in count.items()}
    return probability

probs = calculate_probabilities(historical_activities)
print(f"Probs", probs)

#Display Results
activity_names = {0: 'Sleep', 1: 'Work', 2: 'Exercise', 3: 'Social', 4: 'Leisure'}
for activity, prob in probs.items():
    print(f" {activity_names[activity]}: {prob:.2%}")

#Visualize
plt.figure(figsize=(10, 5))
activities = [activity_names[k] for k in sorted(probs.keys())]
probabilities = [probs[k] for k in sorted(probs.keys())]
plt.bar(activities, probabilities, color='steelblue')
plt.title('Digital Twin: Activity Prediction Probabilities')
plt.ylabel('Probability')
plt.xlabel('Activity')
plt.ylim(0, 0.5)

for i, v in enumerate(probabilities):
    plt.text(i, v + 001, f'{v:.1%}', ha='center')
plt.show()