from flask import Flask, render_template, request, session, redirect, url_for,jsonify
import utils.checkFileName as cfn
import utils.record as record
app = Flask(__name__)
record_job = record.Records()

@app.route('/')
def hello_world():
    return render_template('checkFileName.html')

@app.route('/checkFileName',methods=['POST'])
def checkFileName():
    fileName = request.form['fileName']
    if(fileName != None):
        checkResult = cfn.checkFileName(fileName)
        if checkResult == True:
            record_job.add_use_times(1)
            return jsonify({"code": 1, "msg": "检测通过"})
        else:
            record_job.add_use_times(1)
            record_job.add_false_times(1)
            return jsonify({"code": 0, "msg": "检测失败"})
    else:
        return jsonify({"code": 0, "msg": "检测失败"})


@app.route('/addUseCount',methods=['POST'])
def addUseCount():
    use_count = request.form['use_count']
    record_job.add_use_times(use_count)
    return jsonify({"code": 1, "msg": "添加成功"})


@app.route('/addFalseCount',methods=['POST'])
def addFalseCount():
    false_count = request.form['false_count']
    record_job.add_false_times(false_count)
    return jsonify({"code": 1, "msg": "添加成功"})


@app.route('/getRecordData',methods=['POST'])
def getRecordData():
    record_data = record_job.get_all_data();
    return jsonify({"code": 1, "msg": record_data})




if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=18080)
    record_job.do_schedule_job()

