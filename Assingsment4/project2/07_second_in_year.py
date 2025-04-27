days_per_year:int = 365
hours_per_day:int= 24
min_per_hours:int = 60
sec_per_min:int= 60
def main():
    print("there are " + str( days_per_year* hours_per_day* min_per_hours* sec_per_min)+"seconds in a year")
if __name__ == "__main__":
    main()