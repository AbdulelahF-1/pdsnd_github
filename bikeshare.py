import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('Hello! Let\'s explore some US bikeshare data! //// Project - 3')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while (True):
        city = input("Enter the city (chicago, new york city, washington) : /// Second modify for P3")
        if (city == 'chicago' or city == 'new york city' or city == 'washington'):
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while (True):
        month = input("Enter the month (all, january, february, ... , june) : /// third modify for P3")
        if (month == 'all' or month == 'january' or month == 'febuary' or month == 'march' or month == 'aprel'
                or month == 'may' or month == 'june'):
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while (True):
        day = input("Enter the day (all, monday, tuesday, ... sunday) : ")
        if (day == 'all' or day == 'monday' or day == 'tuesday' or day == 'wednesday' or day == 'thursday'
                or day == 'friday' or day == 'sunday'):
            break

    print('-' * 40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        month = month.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    m_com_month = df['month'].value_counts().idxmax()
    print("The most common month is :", m_com_month)

    # TO DO: display the most common day of week
    m_com_day_of_week = df['day_of_week'].value_counts().idxmax()
    print("The most common day of week is :", m_com_day_of_week)

    # TO DO: display the most common start hour
    m_com_start_hour = df['hour'].value_counts().idxmax()
    print("The most common start hour is :", m_com_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    m_com_start_station = df['Start Station'].value_counts().idxmax()
    print("The most commonly used start station :", m_com_start_station)

    # TO DO: display most commonly used end station
    m_com_end_station = df['End Station'].value_counts().idxmax()
    print("The most commonly used end station :", m_com_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    m_com_start_end_station = df[['Start Station', 'End Station']].mode().loc[0]
    print("The most commonly used start station and end station : ", m_com_start_end_station[0],
          m_com_start_end_station[1])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    print("Total travel time :", total_travel)

    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print("Mean travel time :", mean_travel)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("Counts of user types:\n")
    user_counts = df['User Type'].value_counts()
    for index, user_count in enumerate(user_counts):
        print("  {}: {}".format(user_counts.index[index], user_count))

        # pr

        # TO DO: Display counts of gender
        gender = df['Gender'].value_counts()
        print("The count of user gender from the given fitered data is: \n" + str(gender))

        # TO DO: Display earliest, most recent, and most common year of birth
        earliest_bir = df['Birth Year'].min()
        mo_recent_bir = df['Birth Year'].max()
        mo_common_bir = df['Birth Year'].mode()[0]
        print('Earliest birth from the given fitered data is: {}\n'.format(earliest_bir))
        print('Most recent birth from the given fitered data is: {}\n'.format(mo_recent_bir))
        print('Most common birth from the given fitered data is: {}\n'.format(mo_common_bir))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()


