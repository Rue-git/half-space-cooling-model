import math
import plotly.express as px
import pandas as pd

# define known variables of equation for half-space cooling model
k = 1.5 * (10 ** (-6))
T1 = 1700
T0 = 275


# define function for solving equation with depth and time as unknown variables
def temp(z, t):
    sqt = math.sqrt(k * t)
    sqt = 2 * sqt

    func = z / sqt
    T = (T1 - T0) * math.erf(func) + T0
    return T


# Ma to seconds = [0, 31536*10**9, 126144*10**9, 283824*10**9, 504576*10**9,
#                  788400*10**9, 1545264*10**9, 2554416*10**9]

depth = range(0, 100001, 2000)

# solve equation for different values of t
Ma_1 = []
for n in depth:
    z = n
    t = 31536 * 10 ** 9
    temperatures = temp(z, t)
    Ma_1.append(temperatures)


Ma_4 = []
for n in depth:
    z = n
    t = 126144 * 10 ** 9
    temperatures = temp(z, t)
    Ma_4.append(temperatures)

Ma_9 = []
for n in depth:
    z = n
    t = 283824 * 10 ** 9
    temperatures = temp(z, t)
    Ma_9.append(temperatures)

Ma_16 = []
for n in depth:
    z = n
    t = 504576 * 10 ** 9
    temperatures = temp(z, t)
    Ma_16.append(temperatures)

Ma_25 = []
for n in depth:
    z = n
    t = 788400 * 10 ** 9
    temperatures = temp(z, t)
    Ma_25.append(temperatures)

Ma_49 = []
for n in depth:
    z = n
    t = 1545264 * 10 ** 9
    temperatures = temp(z, t)
    Ma_49.append(temperatures)

Ma_81 = []
for n in depth:
    z = n
    t = 2554416 * 10 ** 9
    temperatures = temp(z, t)
    Ma_81.append(temperatures)

# print(Ma_1, '\n', Ma_4, '\n', Ma_9, '\n', Ma_16, '\n', Ma_25, '\n', Ma_49, '\n', Ma_81, '\n')

# Make pandas dataframe to make results readable
df = pd.DataFrame({'Depth (m)': depth, '1 Ma': Ma_1, '4 Ma': Ma_4, '9 Ma': Ma_9,
                   '16 Ma': Ma_16, '25 Ma': Ma_25, '49 Ma': Ma_49, '81 Ma': Ma_81})

# Export dataframe to excel file
df.to_excel('half-space cooling model.xlsx', sheet_name='temperatures')

# Convert wide data to long data for plotting
df = pd.melt(df, id_vars='Depth (m)', value_vars=df.columns)
df.rename(columns={'value': 'Temperature (K)', 'variable': 'Age'}, inplace=True)
print(df)

# Plot interactive graph
fig = px.line(df, x='Depth (m)', y='Temperature (K)', color='Age')
fig.write_html("file.html")

