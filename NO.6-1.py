while True:
    a=input('a，是否认罪，请回答是或者不是')
    b=input('b，是否认罪，请回答是或者不是')
    if a=='是' and b=='是':
        print('两人各判十年')
    elif a=='不是' and b=='是':
        print('b判1年，a判20年')
    elif a=='是' and b=='不是':
        print('a判1年，b判20年')
    else:
        print('各判3年')
        break


