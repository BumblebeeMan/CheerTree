#!/usr/bin/env python

class CheerTree:
    import requests
    from tree import RGBXmasTree

    tree = RGBXmasTree(brightness=0.1)

    __hexColorPath__ = "http://api.thingspeak.com/channels/1417/field/2/last.txt"

    __lastColor__ = (1, 1, 1)

    __HEADER__={
            "Accept-Encoding": "gzip,deflate,sdch",
            "Accept-Language": "en-US,en;q=0.8",
            "User-Agent": "Chrome/33.0.1750.152",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive"}

    def __init__(self):
        """
        Contructor.
        """
        self.updateTree()

    def __convertHexStringToFloat__(self, hexStr):
        colorInt = int(hexStr, 16)
        if colorInt == 0:
            return 0
        else:
            return (colorInt / 255)

    def __loadColorValue__(self):
        """ 
        
        """
        # Get current color value from Cheerlights API
        response = self.requests.get(self.__hexColorPath__, headers=self.__HEADER__)
        colorStr = str(response.content)
        response.close()
        colorStr = colorStr[3:9]
        print(colorStr)
        if len(colorStr) == 6: # color string contains exactly 6 hex letters
            # convert each color to a value 0 to 1
            r = self.__convertHexStringToFloat__(colorStr[0:2])
            g = self.__convertHexStringToFloat__(colorStr[2:4])
            b = self.__convertHexStringToFloat__(colorStr[4:6])
            print(f"Red {r}, Green {g}, Blue {b}")
            self.__lastColor__ = (r, g, b)
    
    def getLastColor(self):
        return self.__lastColor__
    
    def updateTree(self):
        self.__loadColorValue__()
        #self.tree.color = self.__lastColor__
        print(f"Color {self.__lastColor__}")

    def automode(self, updateTimingSec = 30, autoShutdown = None):
        import time
        while True:
            self.updateTree()
            time.sleep(updateTimingSec)
            #if autoShutdown is not None:
            #    #implement auto shutdown
            #    #self.tree.close()
            #    from subprocess import call
            #    call("shutdown -h now", shell=True)


if __name__ == '__main__':
    tree = CheerTree()
    tree.automode(updateTimingSec = 1, autoShutdown = 1)
