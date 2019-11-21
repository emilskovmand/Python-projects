# PROTOTYPE
The Python file will search through our txt file and find the words and give it its estimated word index:

    "socrates",
    "critias",
    "timaeus",
    "hermocrates",
    "plato"
    
If two words are within a range of 600 of each other in the text, the counter will count it for each conclusion
    "Socrates & Critias: ",
    "Socrates & Timaeus: ",
    "Socrates & Hermocrates: ",
    "Socrates & Plato: ",
    "Critias & Timaeus: "
    "Critias & Hermocrates:
    "Critias & Plato: ",
    "Timaeus & Hermocrates: ",
    "Timaeus & Plato: ",
    "Hermocrates & Plato: "
    
    
The terminals output : 

  Disse ord er indenfor en rækkevidde på 600 ord af hinanden.
  
  Socrates & Critias: 263
  
  Socrates & Timaeus: 342
  
  Socrates & Hermocrates: 71
  
  Socrates & Plato: 19
  
  Critias & Timaeus: 6
  
  Critias & Hermocrates: 11
  
  Critias & Plato: 2
  
  Timaeus & Hermocrates: 70
  
  Timaeus & Plato: 20
  
  Hermocrates & Plato: 2
