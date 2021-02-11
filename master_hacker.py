import time
import random
import progressbar
import math

def master_hacker_two():
   print('\n\n\nWelcome Master Hacker')
   print("Now initiating Master Hacker Program")
   print("Your enemies just lost all hope. \n")
   places_to_hack_today = ['Bank', 'FBI', 'CIA', 'Chinese Government',
                           'NSA', 'University of California Berkeley',
                           'IRS', 'German Government', 'Stock Market',
                           'Google Search Engine', 'Facebook', 'Apple Store',
                           'Russian Hackers']
   while True:
       place_to_hack = places_to_hack_today[random.randint(0, len(places_to_hack_today) - 1)]
       print("Now hacking the : " + place_to_hack)
       hack_one_place(place_to_hack)
       print("\n \n hacking complete\n")
       #for _ in range(10):
       #    time.sleep(0.5)
       #    print("master hacker")


def hack_one_place(places_to_hack):
    arethmatic_series = [0, 0.5]
    a_k = 0.5
    a_r = 0.5
    for k in range(10):
        a_r = a_r*0.5
        a_k += a_r
        arethmatic_series.append(a_k)
    arethmatic_series.append(1)

    bar = progressbar.ProgressBar(redirect_stdout=True, max_value=100)
    for i, a_i in enumerate(arethmatic_series):
        floor = math.floor(a_i*100)
        bar.update(floor)
        time.sleep(0.85)




def master_hacker_one():
    while True:
        time.sleep(0.5)
        print("master hacker")


if __name__ == '__main__':
    master_hacker_two()