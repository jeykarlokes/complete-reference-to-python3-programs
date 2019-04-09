time = input().split(':')
# print(time)
hour_str = time[0]
hour = int(time[0])
minutes = (time[1])
twenty_hour = []
# print(hour,minutes)
sec = time[2]
value_p = any(char for char in sec if char=="P")
value_a = any(char for char in sec if char=="A")

sec =time[2].split("PM")
sec1 = time[2].split("AM")
# print(sec1)
# print(value)
if value_p == True:
    if hour < 12 and hour >= 1 :
        result_time = hour + 12
        twenty_hour.append(result_time)
        twenty_hour.append(minutes)
        twenty_hour.append((sec[0]))
    else:
        twenty_hour.append(time[0])
        twenty_hour.append(minutes)
        twenty_hour.append((sec[0]))
        
elif time[0] == "12":
    twenty_hour.append("00")
    twenty_hour.append(minutes)
    twenty_hour.append((sec1[0]))
else:

    twenty_hour.append(hour_str)
    twenty_hour.append(minutes)
    twenty_hour.append((sec1[0]))
    
twenty_hour = [ str(char) for char in twenty_hour]
new_format = ":".join(twenty_hour)
print(new_format)

