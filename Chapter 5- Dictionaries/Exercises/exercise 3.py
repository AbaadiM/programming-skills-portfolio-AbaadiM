glossary = {
  'List': " A container that can store any kind of values. You can create a list with square brackets", 
  'Comments': "Comments are code lines that will not be executed",
  'Arithmetic Operators': "Assignment operators are use to assign values to variables", 
  'Dictionary' : "A dictionary is an unordered, and changeable, collection",
  'Set': "A set is an unordered, and unchangeable, collection", 
  'indentation' : "Indentation refers to the spaces at the beginning of a code line.", 
  'string': "A series of characters.",
  'print' : "The print() function literally prints the result to the screen.",
  'input' : "It allows us to get input from the user.",
  'Int' :	"The integer number type.",
   }


for word,definition in glossary.items():
    print( word.title() + " : " + definition)