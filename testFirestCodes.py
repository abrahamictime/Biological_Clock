 # how can we develop similar code for the biological arabic time invention?
 print(" why not, let us give it a try!   ")
 
 import pandas as pd
import matplotlib.pyplot as plt

file_path = "masdarData.csv"
df = pd.read_csv(file_path)
print(df.head())

def time_to_seconds(time_str):
    h, m, s = map(int, time_str.split(":"))
    total_seconds = h * 3600 + m * 60 + s
    return total_seconds

def change_sign(row):
    if row['dayOrNight'] == 'night':
        return -row['TimeInSeconds']
    else:
        return row['TimeInSeconds']

# Apply the conversion function to the 'Time' column and create a new 'TimeInSeconds' column
df['TimeInSeconds'] = df['bioTime'].apply(time_to_seconds)

a=df["TimeS"]= df['Time'].apply(time_to_seconds)
# Apply the function to create a new column 'ModifiedTimeInSeconds'
df['BioTimeInSeconds'] = df.apply(change_sign, axis=1)
# for i in a:
#     print(i)

# Plot the data
plt.figure(figsize=(10, 6))  # Optional: Set the figure size
# plt.plot(df.index, df['Relative Humidity'], label='Relative Humidity')
# plt.plot(df.index, df['Temperature'], label='Temperature')
#play with the abit to clarity
plt.plot(df.index, df['TimeS']-44000, label='Normal Times')
plt.plot(df.index, df['BioTimeInSeconds'], label='BioTime')
# plt.plot(df.index, (df['BioTimeInSeconds']//3600)+25, label='BioTime')
# Add labels and title
plt.xlabel('index')
plt.ylabel('Value')
plt.title('Wind Tower Data')

plt.xticks(rotation=45)

# Add legend
plt.legend()

# Show the plot
plt.tight_layout()
plt.grid(True)
plt.show()

