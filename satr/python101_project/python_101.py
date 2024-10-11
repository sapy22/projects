# storage
phone_numbers_list = []
phone_numbers_list.append({'name':'ali',"number":'111111'})
phone_numbers_list.append({'name':'saeed',"number":'222222'})


# functions
def list_all(list):
    return list

def find_record_by_number(number,list):
    for r in list:
        if r['number'] == number:
            return r
    return None

def add_new_record(record,list):
    list.append(record)
    return True

def delete_record_by_number(number,list):
    r = find_record_by_number(number,list)
    if r:
        list.remove(r)
        return True
    return False


# main program
while True:
    print('')
    print('########################## welcome to phone numbers managment system ####################################')
    print('### type (all) to list all records, (f) to find a record by a phone number, (a) to add a new record, (d) to delete a record, (x) to exit the program ###')
    print('')

    command = input('please input a command: ')
    #
    if command == 'all':
        rlist = list_all(phone_numbers_list)
        print('')
        if rlist:
            print('record count',len(rlist))
            for r in rlist:
                print(f"# name = {r['name']}, phone number = {r['number']}")
        else:
            print('there is no record')
        print('')
    #
    elif command == 'f':
        while True:
            num = input('to find a record input (1) or (0) to return: ')
            if num == '0':
                break
            elif num == '1':
                number = input('please input a phone number: ')
                if len(number) == 6 and number.isdigit():
                    r = find_record_by_number(number,phone_numbers_list)
                    print()
                    if r:
                        print(f"# name = {r['name']}, phone number = {r['number']}")
                    else:
                        print('record does not exist')
                    print()
                else:
                    print('this is invalid number, please type 6 digit phone number')  
    #   
    elif command == 'a':
        while True:
            num = input('to add a new record input (1) or (0) to return: ')
            if num == '0':
                break
            elif num == '1':
                number = input('please input the new record phone number: ')
                if len(number) == 6 and number.isdigit():
                    name = input('please input the new record name: ')
                    record = {}
                    record['name'] = name
                    record['number'] = number
                    r = add_new_record(record,phone_numbers_list)
                    if r:
                        print('record added')
                else:
                    print('this is invalid number, please type 6 digit phone number')   
    #
    elif command == 'd':
        while True:
            num = input('to delete a record input (1) or (0) to return: ')
            if num == '0':
                break
            elif num == '1':
                number = input('please input a phone number: ')
                if len(number) == 6 and number.isdigit():
                    r = delete_record_by_number(number,phone_numbers_list)
                    if r:
                        print('record deleted')
                    else:
                        print('record does not exist')
                else:
                    print('this is invalid number, please type 6 digit phone number') 
    #           
    elif command == 'x':
        exit()