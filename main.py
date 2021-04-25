from flask import Flask
from flask import Flask, render_template, request, url_for, jsonify,Response
from  getInfo import getUrl,getImg
from  processImg import detectionPart,ocrPart,multimodalFusion
app = Flask(__name__)
def return_img_stream(img_local_path):
  """
  工具函数:
  获取本地图片流
  :param img_local_path:文件单张图片的本地绝对路径
  :return: 图片流
  """
  import base64
  img_stream = ''
  with open(img_local_path, 'r') as img_f:
    img_stream = img_f.read()
    img_stream = base64.b64encode(img_stream)
  return img_stream
@app.route('/image/<imagePath>')
def getImg(imagePath):
    file=("./image/imagePath".format(imagePath))
    with open(file,'rb') as f:
        image=f.read()
    resp = Response(image, mimetype="image/jpeg")
    return resp
@app.route('/index')
def index():
    return 'Hello World'
@app.route('/')
def hello_world():
    return render_template('content/content.html')
@app.route('/submit',methods=['POST','GET'])
def submit():
    try:
        if request.method=='POST':
            name=request.form['name']
            url=getUrl(name)
            dirPath=getImg(name,url)
            DIR_DETECTION=detectionPart(dirPath)
            DIR_OCR=ocrPart(dirPath)
            pointList,imgPathList,finalPointList=multimodalFusion(DIR_OCR,DIR_DETECTION)


            return render_template('content/content.html',imgPathList=imgPathList,pointList=pointList, finalPointList=finalPointList)
    except:
        return render_template('content/error.html')
# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    app.run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
