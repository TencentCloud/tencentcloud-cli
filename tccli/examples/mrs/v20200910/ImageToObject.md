**Example 1: 图片结构化**

输入一张图片，得到结构化结果

Input: 

```
tccli mrs ImageToObject --cli-unfold-argument  \
    --IsUsedClassify True \
    --Type 0 \
    --UserType 0 \
    --HandleParam.OcrEngineType 2 \
    --HandleParam.IsScale False \
    --HandleParam.ImageOriginalSize 310006 \
    --HandleParam.AutoFitDirection False \
    --HandleParam.IsReturnText False \
    --HandleParam.ScaleTargetSize 300000 \
    --HandleParam.AutoOptimizeCoordinate True \
    --HandleParam.RotateTheAngle 0.0 \
    --ImageInfoList.0.Base64 注意替换为医疗报告图片base64编码 \
    --ImageInfoList.0.Id 1
```

Output: 
```
{
    "Response": {
        "RequestId": "2835bab6-1992-4377-bab4-88e1a8a7adfb",
        "Template": {
            "Indicator": {
                "Indicators": [
                    {
                        "Code": "HBA",
                        "Id": 911,
                        "ItemString": "血红蛋白A",
                        "Name": "血红蛋白A",
                        "Normal": true,
                        "Range": ">94.5",
                        "Scode": "HbA",
                        "Sname": "血红蛋白A",
                        "Unit": "%"
                    },
                    {
                        "Code": "HBF",
                        "Id": 912,
                        "ItemString": "血红蛋白F",
                        "Name": "血红蛋白F",
                        "Normal": true,
                        "Range": "<2.3",
                        "Scode": "HBF",
                        "Sname": "抗碱性血红蛋白",
                        "Unit": "%"
                    },
                    {
                        "Code": "HBA2",
                        "Id": 910,
                        "ItemString": "血红蛋白A2",
                        "Name": "血红蛋白A2",
                        "Normal": true,
                        "Range": "2.5--3.5",
                        "Scode": "HbA2",
                        "Sname": "血红蛋白A2",
                        "Unit": "%"
                    },
                    {
                        "Code": "HBH",
                        "ItemString": "血红蛋白H",
                        "Name": "血红蛋白?",
                        "Normal": true,
                        "Unit": "%"
                    },
                    {
                        "Code": "HBART'S",
                        "ItemString": "血红蛋白Bart's",
                        "Name": "血红蛋白Bart's?",
                        "Normal": true,
                        "Unit": "%"
                    },
                    {
                        "Code": "HBJ",
                        "ItemString": "血红蛋白J",
                        "Name": "血红蛋白?",
                        "Normal": true,
                        "Unit": "%"
                    },
                    {
                        "Code": "HBC-S",
                        "ItemString": "血红蛋白C-S",
                        "Name": "RBC血红蛋白?",
                        "Normal": true,
                        "Unit": "%"
                    },
                    {
                        "Code": "HBE",
                        "ItemString": "血红蛋白E",
                        "Name": "血红蛋白?",
                        "Normal": true,
                        "Unit": "%"
                    },
                    {
                        "Code": "HBS",
                        "ItemString": "血红蛋白S",
                        "Name": "血红蛋白?",
                        "Normal": true,
                        "Unit": "%"
                    },
                    {
                        "Code": "HBD",
                        "ItemString": "血红蛋白D",
                        "Name": "血红蛋白?",
                        "Normal": true,
                        "Unit": "%"
                    },
                    {
                        "Code": "HBG",
                        "ItemString": "血红蛋白G",
                        "Name": "血红蛋白?",
                        "Normal": true,
                        "Unit": "%"
                    },
                    {
                        "Code": "HBK",
                        "ItemString": "血红蛋白K",
                        "Name": "血红蛋白?",
                        "Normal": true,
                        "Unit": "%"
                    },
                    {
                        "Code": "HBOTHERS",
                        "ItemString": "其他异常血红蛋白。",
                        "Name": "其他异常血红蛋白。?",
                        "Normal": true,
                        "Unit": "%"
                    }
                ]
            },
            "OcrResult": "                                                                                                                           ..l2c\n                                                                                                                                     效有日当票\n                                                                                                                           H91 90\n                                                                                                                                       WJ^((9\n                                                                                                                                      M4ohCt\n代号\t项目名称\t结果\t单位\t参考值\t\nHbA\t血红蛋白A\t96.31\t%\t>94.5\t\nHbF\t血红蛋白F\t1.05\t%\t<2.3\t\nHbA2\t血红蛋白A2\t2.64\t%\t2.5~3.5\t\nHbH\t血红蛋白H\t未检出\t%\t\t\nHbarts\t血红蛋白Barts\t未检出\t%\t\t\nHbJ\t血红蛋白J\t未检出\t%\t\t\nHbC-S\t血红蛋白C-S\t未检出\t%\t\t\nHbE\t血红蛋白E\t未检出\t%\t\t\nHbS\t血红蛋白S\t未检出\t%\t\t\nHbD\t血红蛋白D\t未检出\t%\t\t\nHbG\t血红蛋白G\t未检出\t%\t\t\nHbK\t血红蛋白K\t未检出\t%\t\t\nHbothers\t其他异常血红蛋白。\t未检出\t%\t\t\n\n                                                                                                                                      wos ro\n                                                                                                                                     0自\n                                                                                                                                             的屏示\n        门诊                          xxx院检验报告单                                 86-1\n                                                                                 全自动毛细管电泳仪-38\n        姓名:  张三                 科室:产科                                  全血\n        性别:  男                      床号:                              标本类型:               标本状态:                         y\n        年龄:                                                                条码号:  xxxx12582  检验备注:\n                 33岁                    病历号:。                             临床诊断:                                                  B楼四\n                                                     15328022                              体检\n                                                                                                                                               产\n                                                                                                                                                大勺\n                                                      2021-10-31 09:41:00                                                 查蝉响\n 申请医师:xxx                       采集时间:                                        检验者: xxx 审核者:\n                                              报告时间:\n        2021-10-31 10:59:32               2021-11-05 11:05:17\n接收时间:                                                                                                                            第1页.共1页\n※本次实验报告仅对本次标本负责。项目前*号标记为广西医院互认项目。※\n",
            "OcrText": "                                                                                                                           ..l2c\n                                                                                                                                     效有日当票\n                                                                                                                           H91 90\n                                                                                                                                       WJ^((9\n                                                                                                                                      M4ohCt\n代号\t项目名称\t结果\t单位\t参考值\t\nHbA\t血红蛋白A\t96.31\t%\t>94.5\t\nHbF\t血红蛋白F\t1.05\t%\t<2.3\t\nHbA2\t血红蛋白A2\t2.64\t%\t2.5~3.5\t\nHbH\t血红蛋白H\t未检出\t%\t\t\nHbarts\t血红蛋白Barts\t未检出\t%\t\t\nHbJ\t血红蛋白J\t未检出\t%\t\t\nHbC-S\t血红蛋白C-S\t未检出\t%\t\t\nHbE\t血红蛋白E\t未检出\t%\t\t\nHbS\t血红蛋白S\t未检出\t%\t\t\nHbD\t血红蛋白D\t未检出\t%\t\t\nHbG\t血红蛋白G\t未检出\t%\t\t\nHbK\t血红蛋白K\t未检出\t%\t\t\nHbothers\t其他异常血红蛋白。\t未检出\t%\t\t\n\n                                                                                                                                      wos ro\n                                                                                                                                     0自\n                                                                                                                                             的屏示\n        门诊                          xxx医院检验报告单                                 86-1\n                                                                                 全自动毛细管电泳仪-38\n        姓名:  张三                 科室:产科                                  全血\n        性别:  男                      床号:                              标本类型:               标本状态:                         y\n        年龄:                                                                条码号:   xxx12582  检验备注:\n                 33岁                    病历号:。                             临床诊断:                                                  B楼四\n                                                     15328022                              体检\n                                                                                                                                               产\n                                                                                                                                                大勺\n                                                      2021-10-31 09:41:00                                                 查蝉响\n 申请医师:xxx                       采集时间:                                        检验者: xxx 审核者:\n                                              报告时间:\n        2021-10-31 10:59:32               2021-11-05 11:05:17\n接收时间:                                                                                                                            第1页.共1页\n※本次实验报告仅对本次标本负责。项目前*号标记为广西医院互认项目。※\n",
            "PatientInfo": {
                "Age": "33岁",
                "AgeNorm": "289080小时",
                "BedNo": "xxx82",
                "Name": "张三",
                "Sex": "男"
            },
            "ReportInfo": {
                "BedNo": "xxx582",
                "DepartmentName": "体检",
                "Hospital": "xxx医院",
                "MedicalRecordNum": "15328022",
                "ReportName": "检验报告单",
                "ReportTime": "2023-11-05 11:05:17",
                "Times": [
                    {
                        "Name": "报告日期",
                        "Value": "2023-11-05 11:05:17"
                    },
                    {
                        "Name": "接收日期",
                        "Value": "2023-10-31 10:59:32"
                    },
                    {
                        "Name": "采集日期",
                        "Value": "2023-10-31 09:41:00"
                    }
                ]
            },
            "ReportType": "indicator"
        },
        "TextTypeList": [
            {
                "Id": 11,
                "Level": 1,
                "Name": "检验报告"
            },
            {
                "Id": 24,
                "Level": 2,
                "Name": "一般检验"
            },
            {
                "Id": 316,
                "Level": 3,
                "Name": "血液一般检查"
            }
        ]
    }
}
```

