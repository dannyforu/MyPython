import csv
import pandas
import os
import numpy as np


class rec_eidAppFile_student:
    def loaddata(self, line):
        self.name = line[1]
        self.studyid = line[2]
        self.ctid = line[3]
        self.sex = line[4]
        return


class eidAppFile_student:
    def __init__(self):
        return

    def loadFromFile(self, pfile):
        self._file = pfile
        (self._filepath, self._filename) = os.path.split(pfile)
        self._csvfile = open(self._file, "r")
        self._lines = csv.DictReader(self._csvfile)
        return

    def printdata(self):
        for recdata in self._lines:
            print(recdata[0])
        return

    def dealdata(self):
        headers = ["姓名", "学籍号", "性别", "出生日期", "民族", "国籍", "政治面貌", "身份证件类型", "身份证件号", "有效起始日期", "有效截止日期", "学校名称",
                   "学校标识码", "籍贯", "入学年月", "学生来源", "学生类别", "年级", "班号", "港澳台侨外", "专业名称", "健康状况", "出生地", "家庭地址", "邮政编码",
                   "联系电话", "电子邮件地址", "户口性质", "入学方式", "就读方式", "是否进城务工人员子女", "是否孤儿", "是否烈士优抚子女", "是否需要申请资助", "是否享受一补",
                   "随班就读", "是否残疾", "联招合作类型", "联招合作学校机构代码", "监护人姓名", "关系", "身份证件类型", "身份证件号码", "有效起始日期", "有效截止日期",
                   "监护人工作单位", "监护人通讯地址", "邮政编码", "联系电话"]
        coltype = {
            "姓名": np.object, "学籍号": np.object, "性别": np.object, "出生日期": np.object, "民族": np.object, "国籍": np.object,
            "政治面貌": np.object, "身份证件类型": np.object, "身份证件号": np.object, "有效起始日期": np.object, "有效截止日期": np.object,
            "学校名称": np.object,
            "学校标识码": np.object, "籍贯": np.object, "入学年月": np.object, "学生来源": np.object, "学生类别": np.object,
            "年级": np.object, "班号": np.object, "港澳台侨外": np.object, "专业名称": np.object, "健康状况": np.object,
            "出生地": np.object, "家庭地址": np.object, "邮政编码": np.object,
            "联系电话": np.object, "电子邮件地址": np.object, "户口性质": np.object, "入学方式": np.object, "就读方式": np.object,
            "是否进城务工人员子女": np.object, "是否孤儿": np.object, "是否烈士优抚子女": np.object, "是否需要申请资助": np.object,
            "是否享受一补": np.object,
            "随班就读": np.object, "是否残疾": np.object, "联招合作类型": np.object, "联招合作学校机构代码": np.object, "监护人姓名": np.object,
            "关系": np.object, "身份证件类型": np.object, "身份证件号码": np.object, "有效起始日期": np.object, "有效截止日期": np.object,
            "监护人工作单位": np.object, "监护人通讯地址": np.object, "邮政编码": np.object, "联系电话": np.object}

        wfile = "D:\data\output\\" + self._filename
        f = open(wfile, 'w', newline='')
        # 标头在这里传入，作为第一行数据
        writer = csv.DictWriter(f, headers)
        writer.writeheader()
        studata1 = {}
        studata2 = {}
        for studata1 in self._lines:
            # 基础信息处理
            studata2["姓名"] = studata1["学生姓名"].replace("\t", "").replace(" ", "")
            studata2["学籍号"] = studata1["学籍号"].replace("\t", "").replace(" ", "")
            if studata1["性别"] == "男":
                studata2["性别"] = "1"
            elif studata1["性别"] == "女":
                studata2["性别"] = "2"
            else:
                studata2["性别"] = "9"
            studata2["出生日期"] = studata1["出生日期"].replace("\t", "").replace(" ", "")
            studata2["民族"] = studata1["民族"].replace("\t", "").replace(" ", "")
            # 转换国籍编码
            if "中国" in studata1["国籍地区"]:
                studata2["国籍"] = "156"
            else:
                studata2["国籍"] = "156"
            # 转换政治面貌编码
            if "群众" in studata1["政治面貌"]:
                studata2["政治面貌"] = "13"
            elif "共产党党员" in studata1["政治面貌"]:
                studata2["政治面貌"] = "01"
            else:
                studata2["学生类别"] = "13"

            studata2["身份证件类型"] = "1"
            studata2["身份证件号"] = studata1["身份证件号"].replace("\t", "").replace(" ", "")
            # 未获取起始日期、终止日期数据，设为缺省值
            studata2["有效起始日期"] = "20180101"
            studata2["有效截止日期"] = "20180101"
            studata2["学校名称"] = studata1["学校名称"].replace("\t", "").replace(" ", "")
            studata2["学校标识码"] = studata1["学校标识码"].replace("\t", "").replace(" ", "")
            # 根据身份证号确定籍贯
            studata2["籍贯"] = studata2["身份证件号"][0:6]
            studata2["入学年月"] = studata1["入学年月"].replace("\t", "").replace(" ", "")
            studata2["学生来源"] = studata1["学生来源"].replace("\t", "").replace(" ", "")
            if studata2["学生来源"] == "":
                studata2["学生来源"] = "1"
            studata2["年级"] = studata1["年级"].replace("\t", "").replace(" ", "")
            studata2["班号"] = studata1["班级"].replace("\t", "").replace(" ", "")
            # 没有学生类别数据，根据年级判断
            if "初中" in studata1["年级"]:
                studata2["学生类别"] = "31100"
            elif "小学" in studata1["年级"]:
                studata2["学生类别"] = "21100"
            else:
                studata2["学生类别"] = "0"
            # 转换港澳台侨外编码
            if "否" in studata1["港澳台侨外"]:
                studata2["港澳台侨外"] = "00"
            elif "香港" in studata1["港澳台侨外"]:
                studata2["港澳台侨外"] = "01"
            elif "澳门" in studata1["港澳台侨外"]:
                studata2["港澳台侨外"] = "03"
            elif "台湾" in studata1["港澳台侨外"]:
                studata2["港澳台侨外"] = "05"
            else:
                studata2["港澳台侨外"] = "99"
            # 基本信息处理完毕
            writer.writerow(studata2)
        # 转换成XLS文件
        f.close()
        csvfile = pandas.read_csv(wfile, encoding='gbk', dtype=coltype)
        (shotname, extension) = os.path.splitext(self._filename)
        xlsfile = "D:\data\\xls\\" + shotname + ".xlsx"
        csvfile.to_excel(xlsfile, sheet_name='sheet1', index=False)
        return
