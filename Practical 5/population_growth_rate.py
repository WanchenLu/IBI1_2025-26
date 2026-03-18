countries = ['UK','China','Italy','Brazil','USA']
pop2024 = [69.2,1410,58.9,212,340.1]
pop2020 = [66.7,1426,59.4,208.6,331.6]
changes = []
for i in range(len(countries)) :
    change = ((pop2024[i]-pop2020[i])/pop2020[i])*100
    changes.append((countries[i],change))
print (changes)
sorted_changes = sorted(changes,key=lambda x: x[1],reverse=True)
print ("in descending order:",sorted_changes)
print ("the country with the largest increase is ",sorted_changes[0][0],", the country with the largest decrease is ",sorted_changes[-1][0])
import matplotlib.pyplot as plt
ind = list(range(len(countries)))
changes_each = [item[1] for item in changes]
pl = plt.bar(ind,changes_each,width=0.35)
plt.axhline(y=0,color='gray',linestyle='--',linewidth=1)
plt.ylabel("Changes(%)")
plt.title("The population changes for contries")
plt.xticks(ind,countries)
plt.yticks(range(-2,4,1))
plt.bar_label(pl,fmt='%.1f')
plt.show()