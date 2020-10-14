    """

    Completed on: 14/10/2020
    Difficulty: Medium
    Url: https://www.hackerrank.com/challenges/the-time-in-words/problem

    """
def timeInWords(h, m):
  number_strings = ['one', 'two', 'three', 'four', 'five', 'six', 'seven',
                    'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen',
                    'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen',
                    'nineteen', 'twenty', 'twenty one', 'twenty two', 'twenty three',
                    'twenty four', 'twenty five', 'twenty six', 'twenty seven', 'twenty eight',
                    'twenty nine']
  string = ''
  hour = number_strings[h - 1]

  if m <= 0:
    string += hour + " o' clock"
    return string

  if m == 1:
    mins = number_strings[m - 1]
    string += mins +' minute past ' + hour
    return string

  if m < 30 and m > 0  and m != 15 and m != 1:  
    mins = number_strings[m - 1]
    string += mins +' minutes past ' + hour
    return string

  if m == 15:
    string += 'quarter past ' + hour
    return string

  if m == 30:
    string += 'half past ' + hour
    return string

  if m == 45:
    hour = number_strings[h]
    string += 'quarter to ' + hour
    return string

  if m > 30 and m != 45:
    hour = number_strings[h]
    mins = number_strings[60-m-1]
    string += mins + ' minutes to ' + hour
    return string


  
def main():
  print(timeInWords(5, 47))


if __name__ == "__main__":
  main()