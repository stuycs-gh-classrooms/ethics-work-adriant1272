def alarm_clock(day, vacation):
  if day==6 and vacation==False:
    return "10:00"
  if (not vacation and day!=0 and day!=6):
    return "7:00"
  elif (vacation and day==0 or day==6):
    return "off"
  return "10:00"