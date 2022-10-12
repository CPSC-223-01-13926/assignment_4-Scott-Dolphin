import weather as w

myFile = 'w.dat'

myChoice = 0
while True:
    print('      *** TUFFY TITAN WEATHER LOGGER MAIN MENU\n')

    print('1. Set data filename')
    print('2. Add Weather Data')
    print('3. Print Daily Report')
    print('4. Print Historical Data')
    print('9. Exit the program\n')

    myChoice = int(input("Enter menu choice:\n>>>"))
    
    if myChoice == 1:
        myFile = input('Enter Data Filename:\n>>>')
        weather = w.read_data(myFile)

    elif myChoice == 2:
        dt = input('Enter date:\n>>>')
        tm = input('Enter time:\n>>>')
        t =int (input('Enter temperature:\n>>>'))
        h = int(input('Enter humidity:\n>>>'))
        r = float(input('Enter rainfall:\n>>>'))
        weather[dt+tm] = {'t':t, 'h':h, 'r':r}
        w.write_data(weather, myFile)

    elif myChoice == 3:
        d = input('Enter Date:\n>>>')

        display = w.report_daily(weather, d)
        print(display)

    elif myChoice == 4:
        display = w.report_historical(weather)
        print(display)

    elif myChoice == 9:
        break