class Jezyki_programowania():
    def __init__(self, jezyki_programowania):
        self.jezyki_programowania = jezyki_programowania
       






class Python:
    nauka = "łatwy"
    zastosowania = "WEB, AI, CyberSecurity, Testing"
    
    
    def __init__(self, nauka, zastosowania):
        self.nauka = nauka
        self.zastosowania = zastosowania
        
        
        
        
        
class JS(Jezyki_programowania):
    
    
    
    def __init__(self, nauka, zastosowania, jezyki_programowania):
        self.nauka = nauka
        self.zastosowania = zastosowania
        super().__init__(jezyki_programowania)
        print(jezyki_programowania)
        
js = JS("łatwa", "Front-End", "ble ble")          