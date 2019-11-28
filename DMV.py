#!/usr/bin/env python
# coding: utf-8

# Import Selenium Libraries:
from selenium import webdriver
from selenium.webdriver.support.ui import Select


# Office Name --> Office Key
officeKeys = {'ALTURAS': '537', 'ARLETA': '587', 'ARVIN': '661', 'AUBURN': '570', 'BAKERSFIELD': '529', 'BAKERSFIELD SW': '679', 'BANNING': '641', 'BARSTOW': '582', 'BELL GARDENS': '576', 'BELLFLOWER': '606', 'BISHOP': '585', 'BLYTHE': '528', 'BRAWLEY': '597', 'CAPITOLA': '550', 'CARMICHAEL' : '625', 'CHICO': '520', 'CHULA VISTA': '613', 'CLOVIS': '580', 'COALINGA': '603', 'COLUSA': '564', 'COMPTON': '581', 'CONCORD': '523', 'CORTE MADERA': '534', 'COSTA MESA': '628', 'CRESCENT CITY': '524', 'CULVER CITY': '514', 'DALY CITY': '599', 'DAVIS': '598', 'DELANO': '615', 'EL CAJON': '669', 'EL CENTRO': '527', 'EL CERRITO': '556', 'EL MONTE': '685', 'EUREKA': '526', 'FAIRFIELD': '621', 'FALL RIVER MILLS': '643', 'FOLSOM': '655', 'FONTANA': '657', 'FORT BRAGG': '590', 'FREMONT': '644', 'FRESNO': '505', 'FRESNO NORTH': '646', 'FULLERTON': '607', 'GARBERVILLE': '627', 'GARDENA CDTC': '498', 'GILROY': '623', 'GLENDALE': '510', 'GOLETA': '670', 'GRANADA HILLS DLPC': '693', 'GRASS VALLEY': '541', 'HANFORD': '565', 'HAWTHORNE': '609', 'HAYWARD': '579', 'HEMET': '635', 'HOLLISTER': '546', 'HOLLYWOOD': '508', 'HOLLYWOOD WEST': '652', 'INDIO': '578', 'INGLEWOOD': '610', 'JACKSON': '521', 'KING CITY': '647', 'LAGUNA HILLS': '605', 'LAKE ISABELLA': '687', 'LAKEPORT': '530', 'LANCASTER': '595', 'LINCOLN PARK': '617', 'LODI': '622', 'LOMPOC': '692', 'LONG BEACH': '507', 'LOS ANGELES': '502', 'LOS BANOS': '650', 'LOS GATOS': '640', 'MADERA': '533', 'MANTECA': '658', 'MARIPOSA': '566', 'MERCED': '536', 'MODESTO': '557', 'MONTEBELLO': '511', 'MOUNT SHASTA': '639', 'NAPA': '540', 'NEEDLES': '584', 'NEWHALL': '662', 'NORCO': '586', 'NOVATO': '686', 'OAKLAND CLAREMONT': '504', 'OAKLAND COLISEUM': '604', 'OCEANSIDE': '596', 'OROVILLE': '522', 'OXNARD': '636', 'PALM DESERT': '683', 'PALM SPRINGS': '659', 'PARADISE': '601', 'PASADENA': '509', 'PASO ROBLES': '574', 'PETALUMA': '634', 'PITTSBURG': '592', 'PLACERVILLE': '525', 'PLEASANTON': '631', 'POMONA': '532', 'PORTERVILLE': '573', 'POWAY': '676', 'QUINCY': '544', 'RANCHO CUCAMONGA': '612', 'REB BLUFF': '558', 'REDDING': '551', 'REDLANDS': '626', 'REDWOOD CITY': '548', 'REEDLEY': '633', 'RIDGECREST': '577', 'RIVERSIDE': '545', 'RIVERSIDE EAST': '656', 'ROCKLIN': '673', 'ROSEVILLE': '543', 'SACRAMENTO': '501', 'SACROMENTO SOUTH': '602', 'SALINAS': '539', 'SAN ANDREAS': '568', 'SAN BERNARDINO': '512', 'SAN CLEMENTE': '648', 'SAN DIEGO': '506', 'SAN DIEGO CLAIREMONT': '519', 'SAN FRANCISCO': '503', 'SAN JOSE': '516', 'SAN JOSE DLPC': '645', 'SAN LUIS OBISPO': '547', 'SAN MARCOS RACHEROS': '689', 'SAN MATEO': '593', 'SAN PEDRO': '619', 'SAN YSIDRO': '677', 'SANTA ANA': '542', 'SANTA BARBARA': '549', 'SANTA CLARA': '632', 'SANTA MARIA': '563', 'SANTA MONICA': '616', 'SANTA PAULA': '630', 'SANTA ROSA': '555', 'SANTA TERESA': '668', 'SEASIDE': '567', 'SHAFTER': '660', 'SIMI VALLEY': '680', 'SONORA': '569', 'SOUTH LAKE TAHOE': '538', 'STANTON DLPC': '698', 'STOCKTON': '517', 'SUSANVILLE': '531', 'TAFT': '575', 'TEMECULA': '672', 'THOUSAND OAKS': '663', 'TORRANCE': '608', 'TRACY': '642', 'TRUCKEE': '513', 'TULARE': '594', 'TULELAKE': '553', 'TURLOCK': '649', 'TWENTYNINE PALMS': '638', 'UKIAH': '535', 'VACAVILLE': '588', 'VALLEJO': '554', 'VAN NUYS': '515', 'VENTURA': '560', 'VICTORVILLE': '629', 'VISALIA': '559', 'WALNUT CREEK': '624', 'WATSONVILLE': '583', 'WEAVERVILLE': '572', 'WEST COVINA': '618', 'WESTMINSTER': '611', 'WHITTIER': '591', 'WILLOWS': '571', 'WINNETKA': '637', 'WOODLAND': '561', 'YREKA': '552', 'YUBA CITY': '562'}


# Information Login Step - Input: City Name
def information_input(city):
    office = browser.find_element_by_id('officeId')
    Select(office).select_by_value(officeKeys[city])
    test_type = browser.find_element_by_id('DT')
    test_type.click()
    first_name = browser.find_element_by_id('firstName')
    first_name.send_keys('JANE')
    last_name = browser.find_element_by_id('lastName')
    last_name.send_keys('DOE')
    dl_number = browser.find_element_by_id('dl_number')
    dl_number.send_keys('X1234567')
    birth = browser.find_element_by_id('birthMonth')
    birth.send_keys('02292000')
    tel = browser.find_element_by_id('areaCode')
    tel.send_keys('5559876543')
    browser.find_element_by_css_selector('.btn-primary').click()
    
# Call Example: information_input('ALTURAS')


# Appointment Select - Appointment Text Read
def parse_appointment():
    appointments = browser.find_element_by_class_name('col-sm-12').find_elements_by_xpath('.//td')[1]
    info = appointments.find_elements_by_xpath('./p')[-1]
    return info.text


# Parse Date Formats
month_to_num = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}

import re
def parse_date_simple(date_string): #Month/Day/Year
    pattern = re.compile("(?P<month>\w*)/(?P<day>\w*)/(?P<year>\w*)")
    match = pattern.match(date_string)
    month = int(match.group("month"))
    day = int(match.group("day"))
    year = int(match.group("year"))
    return (month, day, year)

def parse_date_complex(date_string): #Month Day, Year at Hour:Minute AM/PM
    pattern = re.compile("(?P<month>\w*)\s(?P<day>\w*),\s(?P<year>\w*)\sat\s(?P<hour>\w*):(?P<minute>\w*)\s(?P<mrdn>\w*)")
    match = pattern.match(date_string)
    month = int(month_to_num[match.group("month")])
    day = int(match.group("day"))
    year = int(match.group("year"))
    hour = int(match.group("hour"))
    minute = int(match.group("minute"))
    mrdn = 0
    if (match.group("mrdn") == 'PM'): mrdn = 1
    return (month, day, year, hour, minute, mrdn)
    
# Simple Call Example: print(parse_date_simple('02/29/2000'))
# Complex Call Example: print(parse_date_complex("Feb 29, 2000 at 12:00 AM"))


# Appointment Search Algorithm - Utilizes provided information from Appointment Text to find all available appointments
def get_all_appointments():
    dates = []
    month = 0
    day = 0
    
    curr_month = browser.find_element_by_class_name('ng_cal_month_table').find_elements_by_xpath('.//td')[13].get_attribute('rel') #i.e. 11/4/15
    curr_month = parse_date_simple(curr_month)[0]
    
    while month < 4:
        # Initialize variables of next available date
        query = parse_appointment()
        if (len(query) > 80):
            return dates
        date_data = parse_date_complex(query)
        month = date_data[0]
        day = date_data[1]
    
        #Go to month and use a reference to calculate corresponding date
        month = (month - curr_month) % 12
        browser.find_element_by_class_name('ng_cal_input_field').click()
        next = browser.find_element_by_class_name("ng_cal_right_month_td") # move across months
        for repeat in range(month):
            next.click()
        calendar_table = browser.find_element_by_class_name('ng_cal_month_table')
        items = calendar_table.find_elements_by_xpath('.//td')
        rel_day = parse_date_simple(items[13].get_attribute('rel'))[1] # day at arbitrary valid position 13 (i.e. 2)
        day = 6 + (day - rel_day) 
            
        time = 800
        while time < 1700:
            item = items[day + 7] # select date
            item.click()
            
            time_string = str(time) # select time
            if (time < 1000):
                time_string = '0' + time_string
            time = browser.find_element_by_id('requestedTime')
            Select(time).select_by_value(time_string)
            browser.find_element_by_id('requestedTime').click() # dummy click to reset
            browser.find_element_by_id("checkAvail").click() # evaluate
                
            # Check status of update appointment times
            query = parse_appointment()

            # Go back to month after query and reupdate assets
            browser.find_element_by_class_name('ng_cal_input_field').click() # date bar
            next = browser.find_element_by_class_name("ng_cal_right_month_td") # move across months
            for repeat in range(month):
                next.click()
            calendar_table = browser.find_element_by_class_name('ng_cal_month_table')
            items = calendar_table.find_elements_by_xpath('.//td')
            
            if (len(query) < 80): # has available slot
                print(query)
                dates.append(query)
                data = parse_date_complex(query)
                time = data[3] * 100 + data[5] * 1200 # hour * 100 + (am/pm) * 1200
                if (data[4] < 30):
                    time += 30
                else :
                    time += 100
            else: # no more slots for this particular day
                break
                
        month, day = go_next_available_day(month, day + 1)
    return dates

# Appointment Search Helper - Go to next available selectable date on calendar
# Input State: Calendar Open at Current Month/Date 
def go_next_available_day(curr_month, curr_day):
    browser.find_element_by_class_name('ng_cal_input_field').click()
    next = browser.find_element_by_class_name("ng_cal_right_month_td")
    while curr_month < 4:
        calendar_table = browser.find_element_by_class_name('ng_cal_month_table')
        items = calendar_table.find_elements_by_xpath('.//td')
        while curr_day < 35:
            item = items[curr_day + 7]
            if ("ng_cal_selectable" in item.get_attribute("class")):
                item.click()
                browser.find_element_by_id('requestedTime').click() # dummy click to reset
                browser.find_element_by_id("checkAvail").click()
                return (curr_month, curr_day)
            curr_day += 1
        next.click()
        curr_day = 0
        curr_month += 1       
    return (curr_month, curr_day)


def main(args):
    if len(args) != 2:
        print("Wrong number of arguments")
        return

    if not officeKeys.contains_key(args[1]):
        print("Location not recognized")
        return

    browser = webdriver.Chrome() # open browser (Chrome)
    browser.get('http://www.dmv.ca.gov/wasapp/foa/driveTest.do') # driving test appointment website
    print(args[1] + ' DMV')
    information_input(args[1])
    print("Total available appointments: ", len(get_all_appointments()))
    browser.quit()

if __name__ == "__main__":
    main(sys.argv)


