def decator(func):

  def obertochka(*args,**kwargs):
    print("Добро пожаловать в....блаблабла\n")
    func(*args,**kwargs)
    print("\n спасибо что посетили.....")
  return obertochka





def table(func):
  def obertochka(*args,**kwargs):
    print("<table>")
    func(*args,**kwargs)
    print("</table>")
  return obertochka


@decator
@table
def say(name,surname,age):
  print("Мистер",name,surname,age)






# t = table(decator(say))
say('vsya','ivanovchenkovo',40)
