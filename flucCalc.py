from datetime import datetime

def flucCalc(glucoseList, startTime_index, bg_index):
  for id, point in enumerate(glucoseList):
    if id == 0:
      previous_point = point
      events = 0  # how many cgm gaps were reviewed
      count = 0
      maxGap = 7  # maximum minute gap between two cgm readings thats accepted; reconfigure for libre users
      continue
    else:
      timeDelta = (datetime.fromisoformat(point[startTime_index]) - datetime.fromisoformat(previous_point[startTime_index])).total_seconds()/60
      if (timeDelta == 0 ) or (timeDelta > maxGap):
        previous_point = point
        continue
      events += 1
      delta = float(point[bg_index]) - float(previous_point[bg_index])
      previous_point = point

      if (delta > 0):
        if (delta / timeDelta) >= (10 / 5):
          count += 1
  rapid_fluc = 100 * count / events

  return rapid_fluc