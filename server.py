from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import socket
import volumeUtility






class Serv(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        try:
            file_to_open = open(self.path[1:],mode = "rb").read()
            
            self.send_response(200)
            
            if self.path[-3:] == "svg":
                self.send_header('Content-type', 'image/svg+xml')
                
            elif self.path[-3:] == "gif":
                self.send_header('Content-type', 'image/gif')
                
            elif self.path[-4:] == "jpeg" or self.path[-3:] == "jpg":
                self.send_header('Content-type', 'image/jpeg')
                
            elif self.path[-3:] == "png":
                self.send_header('Content-type', 'image/png')
                
            elif self.path[-4:] == "html":
                self.send_header('Content-type', 'text/html')
                
            elif self.path[-3:] == "css" or self.path[-7:-4] == "css" :
                self.send_header('Content-type', 'text/css')
            
        except:
            file_to_open = "File not found"
            self.send_response(404)
        self.end_headers()
        self.wfile.write(file_to_open)


    def dataPrepare(self,dataRaw):
        content_length = int(dataRaw.headers['Content-Length'])
        
        data = dataRaw.rfile.read(content_length).decode("utf-8").split("&")

        dataReturn = {}
        for i in range(len(data)):
            temp = data[i].split("=")
            dataReturn[temp[0]]=temp[1]

        return dataReturn

    def action(self):
        pass
            
    def do_POST(self):
        

        data = self.dataPrepare(self)

        response = ""


        if data["action"] == "getVolume":
            response = volumeUtility.volumeLevelStatus()
            self.send_response(201)
            
        elif data["action"] == "increaseVolume":
            response = volumeUtility.increaseVolume()
            self.send_response(201)
            
        elif data["action"] == "decreaseVolume":
            response = volumeUtility.decreaseVolume()
            self.send_response(201)
            
        elif data["action"] == "toggleMute":
            response = volumeUtility.muteVolume();
            self.send_response(201)
            
        elif data["action"] == "togglePlayPause":
            response = volumeUtility.playPause();
            self.send_response(201)
            
        elif data["action"] == "skipNext":
            response = volumeUtility.skipNext();
            self.send_response(201)
            
        elif data["action"] == "skipPrevious":
            response = volumeUtility.skipPrevious();
            self.send_response(201)
            
        else:
            self.send_response(404)
            
        self.end_headers()

        if response == True:
            response = "1"
        elif response == False:
            response = "0"

        self.wfile.write(response.encode())
        pass

host = "0.0.0.0"

httpd = HTTPServer((host, 8080), Serv)
httpd.serve_forever()
