import pandas as pd
import matplotlib.pyplot as plt

# load rankings data here:
wood = pd.read_csv('Golden_Ticket_Award_Winners_Wood.csv')
steel = pd.read_csv('Golden_Ticket_Award_Winners_Steel.csv')


# print(wood.head(), steel.head())
# print(wood[wood["Name"] == 'Boulder Dash'].head(10))


# write function to plot rankings over time for 1 roller coaster here:

def ranking(rc_name, park, data):
    rc = data[(data["Name"] == rc_name) & (data["Park"] == park)]
    fig, ax = plt.subplots()
    ax.plot(rc["Year of Rank"], rc["Rank"])
    ax.invert_yaxis()
    plt.title(rc_name + " rank")
    plt.ylabel("Rank")
    plt.xlabel("Years")
    plt.show()


# ranking("El Toro", "Six Flags Great Adventure", wood)


plt.clf()

# write function to plot rankings over time for 2 roller coasters here:


def ranking_more(rc1_name, park1, rc2_name, park2, data):
    rc1 = data[(data["Name"] == rc1_name) & (data['Park'] == park1)]
    rc2 = data[(data["Name"] == rc2_name) & (data['Park'] == park2)]
    fig, ax = plt.subplots()
    ax.plot(rc1["Year of Rank"], rc1["Rank"], label=rc1_name)
    ax.plot(rc2["Year of Rank"], label=rc2_name)
    ax.invert_yaxis()
    plt.ylabel("Rank")
    plt.xlabel("Years")
    plt.legend()
    plt.show()


# ranking_more("El Toro", "Six Flags Great Adventure", "Boulder Dash", "Lake Compounce", wood)


plt.clf()

# write function to plot top n rankings over time here:


def n_ranking(n, data):
    df = data[data["Rank"] <= n]
    fig, ax = plt.subplots()
    for coaster in set(df["Name"]):
        coaster_rankings = df[df["Name"] == coaster]
        ax.plot(coaster_rankings["Year of Rank"], coaster_rankings["Rank"], "o-", label=coaster)
    ax.invert_yaxis()
    plt.ylabel("Rank")
    plt.xlabel("Years")
    plt.legend(bbox_to_anchor=(1, 1), loc='upper left')
    plt.show()


# n_ranking(5, wood)

plt.clf()


# load roller coaster data here:
captain = pd.read_csv("roller_coasters.csv")
print(captain.head())


# write function to plot histogram of column values here:

def column_hist(data, column):
    plt.hist(data[column].dropna())
    plt.xlabel(column)
    plt.show()


# column_hist(captain, "height")


plt.clf()


# write function to plot inversions by coaster at a park here:

def bar_inversions(data, park):
    park_coasters = data[data["park"] == park]
    park_coasters = park_coasters.sort_values('num_inversions', ascending=False)
    names = park_coasters["name"]
    inversions = park_coasters['num_inversions']
    ax = plt.subplot()
    ax.set_xticks(range(len(names)))
    ax.set_xticklabels(names, rotation=90)
    plt.xlabel("RC names")
    plt.ylabel("inversions")
    plt.bar(range(len(inversions)), inversions)
    plt.show()


# bar_inversions(captain, "Walygator Parc")


plt.clf()


# write function to plot pie chart of operating status here:


def pie_status(df):
    oper = df[df['status'] == 'status.operating']
    closed = df[df['status'] == 'status.closed.definitely']
    numbers = [len(oper), len(closed)]
    explode = (0.1, 0.1)
    plt.pie(numbers, explode=explode, labels=['Operating', 'Closed'], autopct='%0.1f%%', shadow=True, startangle=90)
    plt.title("Работают / не работают")
    plt.axis('equal')
    plt.legend()
    plt.show()


pie_status(captain)

plt.clf()

# write function to create scatter plot of any two numeric columns here:


plt.clf()
