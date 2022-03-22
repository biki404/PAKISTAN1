import requests
bit = platform.architecture()[0]
if bit == '64bit':
    from Lib_biki import main
    main()
elif bit == '32bit':
    print "\x1b[1;91mOpps Sorry Brother Your Mobile Not Support This Tools"
