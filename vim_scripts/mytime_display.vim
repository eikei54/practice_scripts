function! Localtime(year, month, day, hour, minute, second)
    " days from 0000/01/01
    let l:year  = a:month < 3 ? a:year - 1   : a:year
    let l:month = a:month < 3 ? 12 + a:month : a:month
    let l:days = 365*l:year + l:year/4 - l:year/100 + l:year/400 + 306*(l:month+1)/10 + a:day - 428

    " days from 0000/01/01 to 1970/01/01
    " 1970/01/01 == 1969/13/01
    let l:ybase = 1969
    let l:mbase = 13
    let l:dbase = 1
    let l:basedays = 365*l:ybase + l:ybase/4 - l:ybase/100 + l:ybase/400 + 306*(l:mbase+1)/10 + l:dbase - 428

    " seconds from 1970/01/01
    return (l:days-l:basedays)*86400 + (a:hour-9)*3600 + a:minute*60 + a:second
endfunction

function! Disptime()
    let l:now = localtime()
    return strftime("%y%m%d_%H%M%S", l:now)
endfunction
