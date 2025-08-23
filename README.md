# Simple Chatbot (Colab)

This Colab has four cells.

1) Run Cell 1 to install google genai  
2) Run Cell 2 to upload your service account JSON  
3) Run Cell 3 to set credentials and create the client  
4) Run Cell 4 to chat in the notebook. Type exit to quit

**Memory behavior**  
This chatbot remembers conversation history during the current run only. It keeps an in memory list to build each next prompt. It does not save messages anywhere and it forgets everything when you restart the runtime or close the notebook.
