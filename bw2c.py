import Algorithmia as Al
import Tkinter as tk
import tkFileDialog
import tkMessageBox

filename = ' '
apiKey = 'simCYVELO8xne0zulFmUw7eB56m1'
client = Al.client(apiKey)
pt = client.dir('data://sampeter027/ProjectPhoebe')

filename = ' '
input_file = None
img = None
algo = None
resimg = None
OutputAPI = None

def getfilename():
    global filename
    filename = tkFileDialog.askopenfilename()


def start_algorithm():
    global input_file, img, algo, resimg, OutputAPI
    print(filename)
    pt.file("input_file.jpg").put(open(filename, "rb").read())
    img = 'data://sampeter027/ProjectPhoebe/input_file.jpg'
    print("Initalising Algorithm....")
    algo = client.algo('deeplearning/ColorfulImageColorization/1.1.7')
    print("Getting Result...")
    result = algo.pipe(img).result
    OutputAPI = result['output']
    print("Data API link : "+OutputAPI)
    print("API output : "+OutputAPI[57:])
    print("Downloading image....")
    resimg = open('output/'+OutputAPI[57:], "wb").write(client.file(OutputAPI).getBytes())
    tkMessageBox.showinfo("Image saved in Output Directory\nFile name:"+OutputAPI[57:])


mainWin = tk.Tk()
msg = tk.Label(mainWin, text=" Colorization Prototype Inteface ")
getImgButton = tk.Button(mainWin, text="Browse Image", command=getfilename)
startAl = tk.Button(mainWin, text="Start Algorithm", command=start_algorithm)
msg.pack(padx=5, pady=10)
getImgButton.pack()
startAl.pack()
mainWin.title('Colourizer prototype')
mainWin.mainloop()


##img = bytearray(open('test_images/test.JPG', "rb").read())
