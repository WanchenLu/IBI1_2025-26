heart_rates = [72,60,126,85,90,59,76,131,88,121,64]
patients = 0
total = 0
for e in heart_rates :
    total += e
    patients += 1
mean = total/patients
print (patients," patients are in the dataset and the mean heart rate is ",mean)
low = 0
normal = 0
high = 0
for e in heart_rates :
    if e < 60 :
        low += 1
    elif e <= 120 :
        normal += 1
    else :
        high += 1
print (low,"patinets in low category, ",normal,"patients in normal category, ",high,"patients in high category")
category = {'low':low,'normal':normal,'high':high}
max_category = max(category,key=category.get)
print (max_category," contains the largest number of patients")
import matplotlib.pyplot as plt
labels = ['low','normal','high']
sizes = [low,normal,high]
plt.pie(sizes,labels=labels,autopct=lambda pct: f'{pct:.1f}% ({int(pct / 100 * patients)})',startangle=90)
plt.title('Number of patients in each category')
plt.axis('equal')
plt.show()