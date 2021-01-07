from lectura import leer
class libros:
  words_book={}

def detectar(input):
  data=leer(input)
  for items in data['valores']:
    patterns=items.split(' ')
    #if len(patterns)==3 and patterns[1]=='is':
    if patterns[0] not in libros.words_book:
      libros.words_book.update({patterns[0]:patterns[2]})
  print(libros.words_book)
  return data



if __name__ == "__main__":
  data=detectar(input)
  #print(data['valores'])
  print(data)
"""
        read the file contents and split them into 3 modules:
        ref_words: glob is I
        price_msgs: glob glob Silver is 34 Credits
        questions: how much is pish tegj glob glob ?
        error_msgs: not understandable msgs
    """