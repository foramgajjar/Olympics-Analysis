import streamlit as st
import pandas as pd
import helper
import preprocessor
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.figure_factory as ff


df = pd.read_csv('athlete_events.csv')
region = pd.read_csv('noc_regions.csv')

df = preprocessor.preprocess(df, region)

st.sidebar.title("Olympics Analysis ")
st.sidebar.image('data:image/png;base64,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')


user_menu = st.sidebar.radio(
    'Select an options',
    ('Medal Tally', 'Overall Analysis', 'Country wise Analysis', 'Athlete wise Analysis')
)

# st.dataframe(df)

if user_menu == 'Medal Tally':
    st.sidebar.header("Medal Tally")
    years, country = helper.country_year_list(df)

    selected_year = st.sidebar.selectbox("Select Years", years)
    selected_country = st.sidebar.selectbox("Select Country", country)

    medal_tally = helper.fetch_medal_tally(df, selected_year, selected_country)
    if selected_year == "Overall" and selected_country == "Overall":
        st.title("Overall Tally")
    if selected_year != "Overall" and selected_country == "Overall":
        st.title("Medal Tally in " + str(selected_year))
    if selected_year == "Overall" and selected_country != "Overall":
        st.title(str(selected_country) + "'s overall performance")

    if selected_year != "Overall" and selected_country != "Overall":
        st.title(str(selected_country) + "'s performance in " + str(selected_year) + " Olympics")
    st.table(medal_tally)

if user_menu == 'Overall Analysis':
    editions = df['Year'].unique().shape[0] - 1
    cities = df['City'].unique().shape[0]
    sports = df['Sport'].unique().shape[0]
    events = df['Event'].unique().shape[0]
    athletes = df['Name'].unique().shape[0]
    nations = df['region'].unique().shape[0]

    st.title("Top Statistics")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("Editions")
        st.title(editions)
    with col2:
        st.header("Hosts")
        st.title(cities)
    with col3:
        st.header("Sports")
        st.title(sports)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("Events")
        st.title(events)
    with col2:
        st.header("Nations")
        st.title(nations)
    with col3:
        st.header("Athletes")
        st.title(athletes)

    nations_over_time = helper.data_over_time(df, 'region')
    fig = px.line(nations_over_time, x="Edition", y="region")
    fig.show()
    st.title("Participating Nations over the Years")
    st.plotly_chart(fig)

    events_over_time = helper.data_over_time(df, 'Event')
    fig = px.line(events_over_time, x="Edition", y="Event")
    fig.show()
    st.title("Events over the Years")
    st.plotly_chart(fig)

    athletes_over_time = helper.data_over_time(df, 'Name')
    fig = px.line(athletes_over_time, x="Edition", y="Name")
    fig.show()
    st.title("Athletes over the Years")
    st.plotly_chart(fig)

    st.title("No. of Events over time(Every Sport)")
    fig, ax = plt.subplots(figsize=(20, 20))
    x = df.drop_duplicates(['Year', 'Sport', 'Event'])
    ax = sns.heatmap(
        x.pivot_table(index='Sport', columns='Year', values='Event', aggfunc='count').fillna(0).astype('int'),
        annot=True)
    st.pyplot(fig)

    st.title('Most successful Athletes')
    sport_list = df['Sport'].unique().tolist()
    sport_list.sort()
    sport_list.insert(0, 'Overall')

    selected_sport = st.selectbox('Select a sport ', sport_list)
    x = helper.most_successful(df, selected_sport)
    st.table(x)

if user_menu == 'Country wise Analysis':
    st.sidebar.title('Country-wise Analysis')

    country_list = df['region'].dropna().unique().tolist()
    country_list.sort()
    selected_country = st.sidebar.selectbox('Select a country', country_list)

    country_df = helper.year_wise_medal_tally(df, selected_country)
    fig = px.line(country_df, x="Year", y="Medal")
    st.title(selected_country + ' Medal Tally over the years')
    st.plotly_chart(fig)

    pt = helper.country_event_heatmap(df, selected_country)

    st.title(selected_country + ' excels in following sports')
    fig, ax = plt.subplots(figsize=(20, 20))
    ax = sns.heatmap(pt, annot=True)
    st.pyplot(fig)

    st.title('Top 10 athletes of ' + selected_country)
    top10_df = helper.most_successful_country_athletes(df,selected_country)
    st.table(top10_df)


if user_menu == 'Athlete wise Analysis':
    athlete_df = df.drop_duplicates(subset=['Name', 'region'])

    x1 = athlete_df['Age'].dropna()
    x2 = athlete_df[athlete_df['Medal'] == 'Gold']['Age'].dropna()
    x3 = athlete_df[athlete_df['Medal'] == 'Silver']['Age'].dropna()
    x4 = athlete_df[athlete_df['Medal'] == 'Bronze']['Age'].dropna()

    fig = ff.create_distplot([x1, x2, x3, x4], ['Overall Age', 'Gold Medalist', 'Silver Medalist', 'Bronze Medalist'],
                             show_hist=False, show_rug=False)
    fig.update_layout(autosize=False,width=800,height=600)
    st.title('Distribution of Age')
    st.plotly_chart(fig)

    x = []
    name = []
    famous_sports = ['Basketball', 'Judo', 'Football', 'Tug-Of-War', 'Athletics',
                     'Swimming', 'Badminton', 'Sailing', 'Gymnastics',
                     'Art Competitions', 'Handball', 'Weightlifting', 'Wrestling',
                     'Water Polo', 'Hockey', 'Rowing', 'Fencing',
                     'Shooting', 'Boxing', 'Taekwondo', 'Cycling', 'Diving', 'Canoeing',
                     'Tennis', 'Golf', 'Softball', 'Archery',
                     'Volleyball', 'Synchronized Swimming', 'Table Tennis', 'Baseball',
                     'Rhythmic Gymnastics', 'Rugby Sevens',
                     'Beach Volleyball', 'Triathlon', 'Rugby', 'Polo', 'Ice Hockey']
    for sport in famous_sports:
        temp_df = athlete_df[athlete_df['Sport'] == sport]
        x.append(temp_df[temp_df['Medal'] == 'Gold']['Age'].dropna())
        name.append(sport)

    fig = ff.create_distplot(x, name, show_hist=False, show_rug=False)
    fig.update_layout(autosize=False, width=1000, height=600)
    st.title("Distribution of Age wrt Sports(Gold Medalist)")
    st.plotly_chart(fig)

    st.title('Height Vs Weight')
    sport_list = df['Sport'].unique().tolist()
    sport_list.sort()
    sport_list.insert(0, 'Overall')

    selected_sport = st.selectbox('Select a sport ', sport_list)
    temp_df = helper.weight_v_height(df, selected_sport)
    fig, ax = plt.subplots()
    ax = sns.scatterplot(temp_df['Weight'],temp_df['Height'],hue=temp_df['Medal'],style=temp_df['Sex'],s=60)

    st.pyplot(fig)

    st.title("Men Vs Women participation over the Years")
    final = helper.men_v_women(df)
    fig = px.line(final, x="Year", y=['Male', 'Female'])
    st.plotly_chart(fig)