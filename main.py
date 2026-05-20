import time
def Menu():
    print('========================\n'
    'Study Session Tracker\n'
    '========================\n\n' \
    '1. Start Session\n' \
    '2. End Session\n' \
    '3. View Sessions\n' \
    '4. Study Statistics\n' \
    '5. Exit\n')
    choice = input('Enter your Choice: ').strip().capitalize()
    print('========================\n')
    return choice
def StartSession(sessions_list: list):
    current_session = dict()
    try:
        current_session['Subject'] = input('Enter the Subject Name: ').strip().capitalize()
        current_session['Date'] = input('Enter the Date of The Session (YYYY-MM-DD): ').strip()
        current_session['Start Time'] = time.time()
        if current_session['Subject'] == '' or current_session['Date'] == '':
            print('Subject and Date cannot be empty! Please Try Again.\n')
            return
        if len(current_session['Date']) != 10 or current_session['Date'][4] != '-' or current_session['Date'][7] != '-':
            print('Invalid Date Format! Please Use YYYY-MM-DD Format.\n')
            return
        sessions_list.append(current_session)
    except:
        print('An Error Occurred! Please Try Again.\n')
    print('Session Started Successfully!\n')
    return sessions_list
def EndSession(sessions_list: list):
    current_session = sessions_list[-1]
    if len(sessions_list) == 0:
        print('No Active Session Found! Please Start a Session First.\n')
        return
    end_time = time.time()
    duration = end_time - current_session['Start Time']
    current_session['Duration'] = int(round(duration / 60, 2))
    print('Session Ended Successfully!\n')
    return sessions_list
def ViewSessions(sessions_list: list):
    if len (sessions_list) == 0:
        print('No Session Found! Please Start and End a Session First.\n')
        return
    for session in sessions_list:
        print(f"{str(session['Date']).ljust(15)}| {str(session['Subject']).ljust(15)}| {str(session['Duration'])} minutes")
sessions_list = list()
while True:
    choice = Menu()
    if choice == '1' or choice == 'Start':
        StartSession(sessions_list)
    elif choice == '2' or choice == 'End':
        EndSession(sessions_list)
    elif choice == '3' or choice == 'View':
        ViewSessions(sessions_list)
    #elif choice == '4' or choice == 'Study':
        #StudyStatistics()
    elif choice == '5' or choice == 'Exit':
        exit()
    elif choice == '6':
        print(sessions_list)