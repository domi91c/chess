import datetime
import os
from datetime import date, timedelta
from random import randint


def write_log(date):
  f = open('log.txt', 'a+')
  f.writelines(date.isoformat() + '\n')
  f.close()

def commit_github(date):
  dstr = str(date).replace('-', '')
  os.system('git add .')
  os.system('git commit --date={0} -m "Update {0}."'.format(dstr))

def transformation(date) -> datetime.date:
  return datetime.timedelta(hours=randint(0, 24), minutes=randint(0, 60), seconds=randint(0, 60))


def daterange(start_date, end_date):
  for n in range(int ((end_date - start_date).days)):
    yield start_date + timedelta(n)


if __name__ == "__main__":
  print("Hello world")
  commit_count = 500

  start_date = date(2019, 10, 1)
  end_date = date(2019, 12, 1)

  for d in daterange(start_date, end_date):
    for i in range(commit_count):
      commit_github(d)

    print(d)

    #   while commit_count > 0:
    #     date = datetime.datetime.strptime(commit_date, '%Y%m%d')
    #     date += transformation(date)

    #     write_log(date)
    #     commit_github(date)

    #     commit_count -= 1
