import matplotlib.pyplot as plt

heart_rates	= [72, 60, 126,85, 90, 59, 76, 131, 88, 121, 64]
num_patients = len(heart_rates)
mean_rate = sum(heart_rates) / num_patients
print(f"there are {num_patients} patients in the data set")
print(f"the mean heart rate is {mean_rate}")

low = 0
normal = 0
high = 0
for a in heart_rates:
    if a < 60:
        low += 1
    elif a >= 60 and a <= 120:
        normal += 1
    else:
        high += 1
print(f"there are {low} patients have low heart rate, {normal} patients have normal heart rate and {high} patients have high heart rate.")
categories = {"low hr": low, "normal hr": normal, "high hr": high}
max_category = max(categories, key=categories.get)
print(f"{max_category} contains the largest number of patients")

labels = ['Low (<60 bpm)', 'Normal (60-120 bpm)', 'High (>120 bpm)']
sizes = [low, normal, high]
colors = ['#ff9999','#66b3ff','#99ff99']

plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.title('Distribution of Resting Heart Rate Categories')
plt.axis('equal')
plt.show()