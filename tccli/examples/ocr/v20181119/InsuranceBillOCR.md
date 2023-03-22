**Example 1: 保险单据识别示例代码**



Input: 

```
tccli ocr InsuranceBillOCR --cli-unfold-argument  \
    --ImageUrl https://xx/a.jpg 
```

Output: 
```
{
    "Response": {
        "InsuranceBillInfos": [
            {
                "Name": "定点医疗机构名称",
                "Value": "北京南郊肿瘤医院"
            },
            {
                "Name": "No",
                "Value": "2000000000000000000"
            },
            {
                "Name": "定点医疗机构编号",
                "Value": "241560156"
            },
            {
                "Name": "公民身份号码",
                "Value": "320000195101010000"
            },
            {
                "Name": "社保卡/手册编号",
                "Value": "32100000000"
            },
            {
                "Name": "单位",
                "Value": "元(保留两位小数)"
            },
            {
                "Name": "姓名",
                "Value": "AMY"
            },
            {
                "Name": "性别",
                "Value": "男"
            },
            {
                "Name": "年龄",
                "Value": "68岁"
            },
            {
                "Name": "病案号",
                "Value": "T000000000"
            },
            {
                "Name": "费用发生时段",
                "Value": "2019-02-06至2019-02-12"
            },
            {
                "Name": "费用总额",
                "Value": "21257.17"
            },
            {
                "Name": "共计(天)",
                "Value": "6"
            },
            {
                "Name": "日均额",
                "Value": "3542.86"
            },
            {
                "Name": "床位费总额",
                "Value": "182.00"
            },
            {
                "Name": "名称",
                "Value": "普通床位费[普通床位费(24)]"
            },
            {
                "Name": "单价",
                "Value": "24.0000"
            },
            {
                "Name": "数量",
                "Value": "7.00"
            },
            {
                "Name": "金额",
                "Value": "168.00"
            },
            {
                "Name": "医保内",
                "Value": "168.00"
            },
            {
                "Name": "医保外",
                "Value": "0.00"
            },
            {
                "Name": "名称",
                "Value": "二级医院住院床位费加收"
            },
            {
                "Name": "单价",
                "Value": "2.0000"
            },
            {
                "Name": "数量",
                "Value": "7.00"
            },
            {
                "Name": "金额",
                "Value": "14.00"
            },
            {
                "Name": "医保内",
                "Value": "14.00"
            },
            {
                "Name": "医保外",
                "Value": "0.00"
            },
            {
                "Name": "护理费总额",
                "Value": "44.00"
            },
            {
                "Name": "名称",
                "Value": "一级护理"
            },
            {
                "Name": "单价",
                "Value": "8.0000"
            },
            {
                "Name": "数量",
                "Value": "1.00"
            },
            {
                "Name": "金额",
                "Value": "8.00"
            },
            {
                "Name": "医保内",
                "Value": "8.00"
            },
            {
                "Name": "医保外",
                "Value": "0.00"
            },
            {
                "Name": "名称",
                "Value": "二级护理"
            },
            {
                "Name": "单价",
                "Value": "6.0000"
            },
            {
                "Name": "数量",
                "Value": "6.00"
            },
            {
                "Name": "金额",
                "Value": "36.00"
            },
            {
                "Name": "医保内",
                "Value": "36.00"
            },
            {
                "Name": "医保外",
                "Value": "0.00"
            },
            {
                "Name": "诊疗费总额",
                "Value": "42.00"
            },
            {
                "Name": "名称",
                "Value": "住院诊疗费(二级医院)"
            },
            {
                "Name": "单价",
                "Value": "6.0000"
            },
            {
                "Name": "数量",
                "Value": "7.00"
            },
            {
                "Name": "金额",
                "Value": "42.00"
            },
            {
                "Name": "医保内",
                "Value": "42.00"
            },
            {
                "Name": "医保外",
                "Value": "0.00"
            },
            {
                "Name": "药费总额",
                "Value": "4526.87"
            },
            {
                "Name": "其中西药费",
                "Value": "4526.87"
            },
            {
                "Name": "其中中成药费",
                "Value": "0.00"
            },
            {
                "Name": "其中中草药费",
                "Value": "0.00"
            },
            {
                "Name": "名称",
                "Value": "吸入用七氟烷"
            },
            {
                "Name": "规格",
                "Value": "1ml"
            },
            {
                "Name": "单价",
                "Value": "7.5400"
            },
            {
                "Name": "数量",
                "Value": "60.00"
            },
            {
                "Name": "金额",
                "Value": "452.40"
            },
            {
                "Name": "医保内",
                "Value": "452.40"
            },
            {
                "Name": "医保外",
                "Value": "0.00"
            },
            {
                "Name": "名称",
                "Value": "依托咪酯注射用乳剂"
            },
            {
                "Name": "规格",
                "Value": "10ml:20mg"
            },
            {
                "Name": "单价",
                "Value": "43.4100"
            },
            {
                "Name": "数量",
                "Value": "1.00"
            },
            {
                "Name": "金额",
                "Value": "43.41"
            },
            {
                "Name": "医保内",
                "Value": "43.41"
            },
            {
                "Name": "医保外",
                "Value": "0.00"
            },
            {
                "Name": "名称",
                "Value": "盐酸利多卡因注射液"
            },
            {
                "Name": "规格",
                "Value": "5ml:0.1g"
            },
            {
                "Name": "单价",
                "Value": "1.5200"
            },
            {
                "Name": "数量",
                "Value": "1.00"
            },
            {
                "Name": "金额",
                "Value": "1.52"
            },
            {
                "Name": "医保内",
                "Value": "1.52"
            },
            {
                "Name": "医保外",
                "Value": "0.00"
            },
            {
                "Name": "名称",
                "Value": "盐酸利多卡因胶浆"
            },
            {
                "Name": "规格",
                "Value": "10g:0.2g"
            },
            {
                "Name": "单价",
                "Value": "7.4280"
            },
            {
                "Name": "数量",
                "Value": "1.00"
            },
            {
                "Name": "金额",
                "Value": "7.43"
            },
            {
                "Name": "医保内",
                "Value": "0.00"
            },
            {
                "Name": "医保外",
                "Value": "7.43"
            },
            {
                "Name": "名称",
                "Value": "维生素C注射液"
            },
            {
                "Name": "规格",
                "Value": "2.5ml:1g"
            },
            {
                "Name": "单价",
                "Value": "0.5700"
            },
            {
                "Name": "数量",
                "Value": "8.00"
            },
            {
                "Name": "金额",
                "Value": "4.56"
            },
            {
                "Name": "医保内",
                "Value": "4.56"
            },
            {
                "Name": "医保外",
                "Value": "0.00"
            },
            {
                "Name": "名称",
                "Value": "地塞米松磷酸钠注射液"
            },
            {
                "Name": "规格",
                "Value": "1ml:5mg"
            },
            {
                "Name": "单价",
                "Value": "0.5100"
            },
            {
                "Name": "数量",
                "Value": "3.00"
            },
            {
                "Name": "金额",
                "Value": "1.53"
            },
            {
                "Name": "医保内",
                "Value": "1.53"
            },
            {
                "Name": "医保外",
                "Value": "0.00"
            },
            {
                "Name": "名称",
                "Value": "左甲状腺素钠片"
            },
            {
                "Name": "规格",
                "Value": "50ug"
            },
            {
                "Name": "单价",
                "Value": "0.3110"
            },
            {
                "Name": "数量",
                "Value": "40.00"
            },
            {
                "Name": "金额",
                "Value": "12.43"
            },
            {
                "Name": "医保内",
                "Value": "12.43"
            },
            {
                "Name": "医保外",
                "Value": "0.00"
            },
            {
                "Name": "名称",
                "Value": "硫酸阿托品注射液"
            },
            {
                "Name": "规格",
                "Value": "1ml:0.5mg"
            },
            {
                "Name": "单价",
                "Value": "0.7500"
            },
            {
                "Name": "数量",
                "Value": "1.00"
            },
            {
                "Name": "金额",
                "Value": "0.75"
            },
            {
                "Name": "医保内",
                "Value": "0.75"
            },
            {
                "Name": "医保外",
                "Value": "0.00"
            },
            {
                "Name": "名称",
                "Value": "盐酸氨溴索注射液"
            },
            {
                "Name": "规格",
                "Value": "2ml:15mg"
            },
            {
                "Name": "单价",
                "Value": "6.2100"
            },
            {
                "Name": "数量",
                "Value": "6.00"
            },
            {
                "Name": "金额",
                "Value": "37.26"
            },
            {
                "Name": "医保内",
                "Value": "0.00"
            },
            {
                "Name": "医保外",
                "Value": "37.26"
            },
            {
                "Name": "名称",
                "Value": "盐酸托烷司琼注射液"
            },
            {
                "Name": "规格",
                "Value": "5ml:5mg"
            },
            {
                "Name": "单价",
                "Value": "97.2900"
            },
            {
                "Name": "数量",
                "Value": "1.00"
            },
            {
                "Name": "金额",
                "Value": "97.29"
            },
            {
                "Name": "医保内",
                "Value": "97.29"
            },
            {
                "Name": "医保外",
                "Value": "0.00"
            },
            {
                "Name": "名称",
                "Value": "乌拉地尔注射液"
            },
            {
                "Name": "规格",
                "Value": "5ml:25mg"
            },
            {
                "Name": "单价",
                "Value": "58.3000"
            },
            {
                "Name": "数量",
                "Value": "1.00"
            },
            {
                "Name": "金额",
                "Value": "58.30"
            },
            {
                "Name": "医保内",
                "Value": "52.47"
            },
            {
                "Name": "医保外",
                "Value": "5.83"
            },
            {
                "Name": "名称",
                "Value": "复方电解质葡萄糖MG3注射液"
            },
            {
                "Name": "规格",
                "Value": "500ml"
            },
            {
                "Name": "单价",
                "Value": "13.2000"
            }
        ],
        "RequestId": "4ff69826-ce50-41f9-acf6-1e37d068fcb8"
    }
}
```

