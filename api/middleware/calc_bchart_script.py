import datetime
import pytz
import sys


"""
Year  rollover - 2월 3일 23시 에
month rollover - [(1, 5), (2, 4), (3, 6), (4, 5), (5, 5), (6, 6), (7, 7), (8, 7), (9, 8), (10, 8), (11, 7), (12, 7)] 에서 하루 전 23시
day rollover 23시
time 은 홀수로 변경

"""
GAN = ["GAP", "EUL", "BYU", "JUN", "MUU", "KII", "KYU", "SHI", "YIM", "KYE"]
JI = ["RAT", "OXX", "TIG", "RAB", "DRA", "SNA", "HOR", "GOA", "MON", "ROO", "DOG", "PIG"]
ZODIAC = {
  "RAT" : "rat",
  "OXX" : "ox", 
  "TIG" : "tiger", 
  "RAB" : "rabbit", 
  "DRA" : "dragon", 
  "SNA" : "snake", 
  "HOR" : "horse", 
  "GOA" : "goat", 
  "MON" : "monkey", 
  "ROO" : "rooster", 
  "DOG" : "dog", 
  "PIG" : "pig",
}

INIT_DATETIME = pytz.UTC.localize(datetime.datetime(1922, 2, 3, 23, 0))
INIT_DATA_19220203_2300 = {
    "year_gan": "YIM",
    "year_ji": "DOG",
    "month_gan": "YIM",
    "month_ji": "TIG",
    "day_gan": "KYE",
    "day_ji": "RAB",
    "time_gan": "YIM",
    "time_ji": "RAT",
}

def get_next_value(list_, meta):
    idx = list_.index(meta)
    if idx == len(list_) - 1:
        next_idx = 0
    else:
        next_idx = idx + 1
    return list_[next_idx]


def get_year_ganji(datetime_, year_gan, year_ji):
    # 2월 4일에 연이 바뀜
    # 정확히 2월 3일 23시에 바뀜
    if datetime_.month == 2 and datetime_.day == 3 \
            and datetime_.hour == 23:
        year_gan = get_next_value(GAN, year_gan)
        year_ji = get_next_value(JI, year_ji)
    return year_gan, year_ji


def get_month_ganji(datetime_, month_gan, month_ji):
    # 1월 5일, 2월 4일, ..., 12월 7일의 전날 23시에 월이 바뀜
    if datetime_.hour == 23 and \
            (datetime_.month, datetime_.day+1) in \
        [(1, 5), (2, 4), (3, 6), (4, 5), (5, 5), (6, 6), (7, 7), (8, 7), (9, 8), (10, 8), (11, 7), (12, 7)]:
        month_gan = get_next_value(GAN, month_gan)
        month_ji = get_next_value(JI, month_ji)
    return month_gan, month_ji


def get_day_ganji(datetime_, day_gan, day_ji):
    # 23시에 바뀜
    if datetime_.hour == 23:
        day_gan = get_next_value(GAN, day_gan)
        day_ji = get_next_value(JI, day_ji)
    return day_gan, day_ji


def get_time_ganji(datetime_, time_gan, time_ji):
    # 1, 3, 5, ..., 23시에 바뀜
    ganji_changes = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]
    if datetime_.hour in ganji_changes:
        time_gan = get_next_value(GAN, time_gan)
        time_ji = get_next_value(JI, time_ji)
    return time_gan, time_ji


def main(date_input):

    # print("init date 1922-02-03 23:00")
    start_datetime = INIT_DATETIME
    start_birthchart = INIT_DATA_19220203_2300


    # print("Start datetime: ", start_datetime)
    # print("Start birthchar: ", start_birthchart)
    end_date_string = date_input

    # print("end data", end_date_string)

    end_datetime = pytz.UTC.localize(datetime.datetime.strptime(end_date_string, "%Y-%m-%d"))
    if end_datetime < start_datetime:
        print(f"{end_datetime} before {start_datetime}")
        return

    # birthchart of the day before start date
    year_gan, year_ji = start_birthchart['year_gan'], start_birthchart['year_ji']
    month_gan, month_ji = start_birthchart['month_gan'], start_birthchart['month_ji']
    day_gan, day_ji = start_birthchart['day_gan'], start_birthchart['day_ji']
    time_gan, time_ji = start_birthchart['time_gan'], start_birthchart['time_ji']

    # initialize data
    td = datetime.timedelta(hours=1)
    datetime_ = start_datetime + td

    while datetime_ < end_datetime:
        year_gan, year_ji = get_year_ganji(datetime_, year_gan, year_ji)
        month_gan, month_ji = get_month_ganji(datetime_, month_gan, month_ji)
        day_gan, day_ji = get_day_ganji(datetime_, day_gan, day_ji)
        time_gan, time_ji = get_time_ganji(datetime_, time_gan, time_ji)
        datetime_ += td
    
    return(ZODIAC[day_ji])



# if __name__ == "__main__":
#     main("1926-12-12")