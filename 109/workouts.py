WORKOUT_SCHEDULE = {'Friday': 'Shoulders',
                    'Monday': 'Chest+biceps',
                    'Saturday': 'Rest',
                    'Sunday': 'Rest',
                    'Thursday': 'Legs',
                    'Tuesday': 'Back+triceps',
                    'Wednesday': 'Core'}
REST, CHILL_OUT, TRAIN = 'Rest', 'Chill out!', 'Go train {}'
INVALID_DAY = 'Not a valid day'


def get_workout_motd(day):
   '''day = day.title()

   for weekday, workout in WORKOUT_SCHEDULE.items():
      if day == weekday and workout == "Rest":
         return(CHILL_OUT)
      elif day == weekday:
         return(TRAIN.format(workout))
   return(INVALID_DAY)'''
   workout = WORKOUT_SCHEDULE.get(day.title())
   if workout is None:
      return INVALID_DAY
   return CHILL_OUT if workout == REST else TRAIN.format(workout)

"""First title case the passed in day argument
       (so monday or MONDAY both result in Monday).

       If day is not in WORKOUT_SCHEDULE, return INVALID_DAY

       If day is in WORKOUT_SCHEDULE retrieve the value (workout)
       and return the following:
       - weekday, return TRAIN with the workout value interpolated
       - weekend day (value 'Rest'), return CHILL_OUT

       Examples:
       - if day is Monday -> function returns 'Go train Chest+biceps'
       - if day is Thursday -> function returns 'Go train Legs'
       - if day is Saturday -> function returns 'Chill out!'
       - if day is nonsense -> function returns 'Not a valid day'

       Trivia: /etc/motd is a file on Unix-like systems that contains
       a 'message of the day'
"""

if __name__=="__main__":
   #print(get_workout_motd("Monday"))
   print(get_workout_motd("sAturdAy"))
   print(get_workout_motd("tuesday"))
