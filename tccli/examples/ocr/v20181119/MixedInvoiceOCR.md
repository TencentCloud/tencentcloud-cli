**Example 1: 混贴票据识别示例代码（识别全部类型）**

混贴票据识别示例代码（识别全部类型）

Input: 

```
tccli ocr MixedInvoiceOCR --cli-unfold-argument  \
    --ImageUrl https://xx/a.jpg
```

Output: 
```
{
    "Response": {
        "MixedInvoiceItems": [
            {
                "Rect": {
                    "X": -19,
                    "Y": 34,
                    "Width": 1399,
                    "Height": 845
                },
                "Angle": 0,
                "Type": 3,
                "Code": "OK",
                "Page": 1,
                "SingleInvoiceInfos": [
                    {
                        "Name": "销售方识别号",
                        "Value": "440300094040109",
                        "Row": -1
                    },
                    {
                        "Name": "销售方名称",
                        "Value": "深圳市游戏科技有限公司",
                        "Row": -1
                    },
                    {
                        "Name": "购买方识别号",
                        "Value": "440300708461136",
                        "Row": -1
                    },
                    {
                        "Name": "购买方名称",
                        "Value": "深圳市腾讯计算机系统有限公司",
                        "Row": -1
                    },
                    {
                        "Name": "发票名称",
                        "Value": "深圳增值税专用发票",
                        "Row": -1
                    },
                    {
                        "Name": "发票代码",
                        "Value": "4403152130",
                        "Row": -1
                    },
                    {
                        "Name": "发票号码",
                        "Value": "No14998456",
                        "Row": -1
                    },
                    {
                        "Name": "打印发票代码",
                        "Value": "4403152130",
                        "Row": -1
                    },
                    {
                        "Name": "打印发票号码",
                        "Value": "No14998456",
                        "Row": -1
                    },
                    {
                        "Name": "开票日期",
                        "Value": "2016年04月11日",
                        "Row": -1
                    },
                    {
                        "Name": "密码区1",
                        "Value": "*7-0<84019---5+68315-99->/51",
                        "Row": -1
                    },
                    {
                        "Name": "密码区2",
                        "Value": ">814<1/7922/<-23/908+>7474+3",
                        "Row": -1
                    },
                    {
                        "Name": "购买方地址、电话",
                        "Value": "深圳市南山区高新区高新南一路飞亚达大厦5-10楼0755-86013388",
                        "Row": -1
                    },
                    {
                        "Name": "密码区3",
                        "Value": "78312-072<3<729-+4<6*315-094",
                        "Row": -1
                    },
                    {
                        "Name": "密码区4",
                        "Value": "->/5>18493/1-60*6-43/90<--78",
                        "Row": -1
                    },
                    {
                        "Name": "购买方开户行及账号",
                        "Value": "招商银行深圳分行振兴支行817282299619961",
                        "Row": -1
                    },
                    {
                        "Name": "货物或应税劳务、服务名称",
                        "Value": "技术服务费",
                        "Row": 0
                    },
                    {
                        "Name": "金额",
                        "Value": "778.44",
                        "Row": 0
                    },
                    {
                        "Name": "税率",
                        "Value": "6%",
                        "Row": 0
                    },
                    {
                        "Name": "税额",
                        "Value": "46.71",
                        "Row": 0
                    },
                    {
                        "Name": "合计金额",
                        "Value": "¥778.44",
                        "Row": -1
                    },
                    {
                        "Name": "合计税额",
                        "Value": "46.71",
                        "Row": -1
                    },
                    {
                        "Name": "价税合计(大写)",
                        "Value": "捌佰贰拾伍圆壹角伍分",
                        "Row": -1
                    },
                    {
                        "Name": "小写金额",
                        "Value": "¥825.15",
                        "Row": -1
                    },
                    {
                        "Name": "销售方地址、电话",
                        "Value": "深圳市南山区高新南一道3号赋安科技大楼A座301室0755-86315454",
                        "Row": -1
                    },
                    {
                        "Name": "销售方开户行及账号",
                        "Value": "浦发行深圳科技园支行79210154740015474",
                        "Row": -1
                    },
                    {
                        "Name": "收款人",
                        "Value": "李明",
                        "Row": -1
                    },
                    {
                        "Name": "复核",
                        "Value": "晓艾",
                        "Row": -1
                    },
                    {
                        "Name": "开票人",
                        "Value": "张三",
                        "Row": -1
                    },
                    {
                        "Name": "是否有公司印章",
                        "Value": "1",
                        "Row": -1
                    },
                    {
                        "Name": "联次",
                        "Value": "三",
                        "Row": -1
                    },
                    {
                        "Name": "省",
                        "Value": "广东省",
                        "Row": -1
                    },
                    {
                        "Name": "市",
                        "Value": "深圳市",
                        "Row": -1
                    },
                    {
                        "Name": "发票消费类型",
                        "Value": "服务",
                        "Row": -1
                    },
                    {
                        "Name": "发票类型",
                        "Value": "增值税专用发票",
                        "Row": -1
                    },
                    {
                        "Name": "机器编号",
                        "Value": "",
                        "Row": -1
                    },
                    {
                        "Name": "校验码",
                        "Value": "",
                        "Row": -1
                    },
                    {
                        "Name": "单价",
                        "Value": "",
                        "Row": -1
                    },
                    {
                        "Name": "备注",
                        "Value": "",
                        "Row": -1
                    },
                    {
                        "Name": "单位",
                        "Value": "",
                        "Row": -1
                    },
                    {
                        "Name": "数量",
                        "Value": "",
                        "Row": -1
                    },
                    {
                        "Name": "规格型号",
                        "Value": "",
                        "Row": -1
                    },
                    {
                        "Name": "是否代开",
                        "Value": "",
                        "Row": -1
                    },
                    {
                        "Name": "成品油标志",
                        "Value": "",
                        "Row": -1
                    },
                    {
                        "Name": "服务类型",
                        "Value": "",
                        "Row": -1
                    },
                    {
                        "Name": "通行费标志",
                        "Value": "",
                        "Row": -1
                    },
                    {
                        "Name": "车船税",
                        "Value": "",
                        "Row": -1
                    },
                    {
                        "Name": "车牌号",
                        "Value": "",
                        "Row": -1
                    },
                    {
                        "Name": "类型",
                        "Value": "",
                        "Row": -1
                    },
                    {
                        "Name": "通行日期起",
                        "Value": "",
                        "Row": -1
                    },
                    {
                        "Name": "通行日期止",
                        "Value": "",
                        "Row": -1
                    }
                ]
            }
        ],
        "RequestId": "3a850dbc-2de1-4dfb-9ecd-7ae57f2fe666"
    }
}
```

**Example 2: 混贴票据识别示例代码（识别指定类型）**

混贴票据识别示例代码（识别指定类型）

Input: 

```
tccli ocr MixedInvoiceOCR --cli-unfold-argument  \
    --ImageUrl https://xx/a.jpg \
    --Types 2
```

Output: 
```
{
    "Response": {
        "MixedInvoiceItems": [
            {
                "Rect": {
                    "X": -19,
                    "Y": 34,
                    "Width": 1399,
                    "Height": 845
                },
                "Angle": 0,
                "Type": 3,
                "Code": "OK",
                "Page": 1,
                "SingleInvoiceInfos": [
                    {
                        "Name": "销售方识别号",
                        "Value": "440300094040109",
                        "Row": -1
                    },
                    {
                        "Name": "销售方名称",
                        "Value": "深圳市游戏科技有限公司",
                        "Row": -1
                    },
                    {
                        "Name": "购买方识别号",
                        "Value": "440300708461136",
                        "Row": -1
                    },
                    {
                        "Name": "购买方名称",
                        "Value": "深圳市腾讯计算机系统有限公司",
                        "Row": -1
                    },
                    {
                        "Name": "发票名称",
                        "Value": "深圳增值税专用发票",
                        "Row": -1
                    },
                    {
                        "Name": "发票代码",
                        "Value": "4403152130",
                        "Row": -1
                    },
                    {
                        "Name": "发票号码",
                        "Value": "No14998456",
                        "Row": -1
                    },
                    {
                        "Name": "打印发票代码",
                        "Value": "4403152130",
                        "Row": -1
                    },
                    {
                        "Name": "打印发票号码",
                        "Value": "No14998456",
                        "Row": -1
                    },
                    {
                        "Name": "开票日期",
                        "Value": "2016年04月11日",
                        "Row": -1
                    },
                    {
                        "Name": "密码区1",
                        "Value": "*7-0<84019---5+68315-99->/51",
                        "Row": -1
                    },
                    {
                        "Name": "密码区2",
                        "Value": ">814<1/7922/<-23/908+>7474+3",
                        "Row": -1
                    },
                    {
                        "Name": "购买方地址、电话",
                        "Value": "深圳市南山区高新区高新南一路飞亚达大厦5-10楼0755-86013388",
                        "Row": -1
                    },
                    {
                        "Name": "密码区3",
                        "Value": "78312-072<3<729-+4<6*315-094",
                        "Row": -1
                    },
                    {
                        "Name": "密码区4",
                        "Value": "->/5>18493/1-60*6-43/90<--78",
                        "Row": -1
                    },
                    {
                        "Name": "购买方开户行及账号",
                        "Value": "招商银行深圳分行振兴支行817282299619961",
                        "Row": -1
                    },
                    {
                        "Name": "货物或应税劳务、服务名称",
                        "Value": "技术服务费",
                        "Row": 0
                    },
                    {
                        "Name": "金额",
                        "Value": "778.44",
                        "Row": 0
                    },
                    {
                        "Name": "税率",
                        "Value": "6%",
                        "Row": 0
                    },
                    {
                        "Name": "税额",
                        "Value": "46.71",
                        "Row": 0
                    },
                    {
                        "Name": "合计金额",
                        "Value": "¥778.44",
                        "Row": -1
                    },
                    {
                        "Name": "合计税额",
                        "Value": "46.71",
                        "Row": -1
                    },
                    {
                        "Name": "价税合计(大写)",
                        "Value": "捌佰贰拾伍圆壹角伍分",
                        "Row": -1
                    },
                    {
                        "Name": "小写金额",
                        "Value": "¥825.15",
                        "Row": -1
                    },
                    {
                        "Name": "销售方地址、电话",
                        "Value": "深圳市南山区高新南一道3号赋安科技大楼A座301室0755-86315454",
                        "Row": -1
                    },
                    {
                        "Name": "销售方开户行及账号",
                        "Value": "浦发行深圳科技园支行79210154740015474",
                        "Row": -1
                    },
                    {
                        "Name": "收款人",
                        "Value": "李明",
                        "Row": -1
                    },
                    {
                        "Name": "复核",
                        "Value": "晓艾",
                        "Row": -1
                    },
                    {
                        "Name": "开票人",
                        "Value": "张三",
                        "Row": -1
                    },
                    {
                        "Name": "是否有公司印章",
                        "Value": "1",
                        "Row": -1
                    },
                    {
                        "Name": "联次",
                        "Value": "三",
                        "Row": -1
                    },
                    {
                        "Name": "省",
                        "Value": "广东省",
                        "Row": -1
                    },
                    {
                        "Name": "市",
                        "Value": "深圳市",
                        "Row": -1
                    },
                    {
                        "Name": "发票消费类型",
                        "Value": "服务",
                        "Row": -1
                    },
                    {
                        "Name": "发票类型",
                        "Value": "增值税专用发票",
                        "Row": -1
                    },
                    {
                        "Name": "机器编号",
                        "Value": "",
                        "Row": -1
                    },
                    {
                        "Name": "校验码",
                        "Value": "",
                        "Row": -1
                    },
                    {
                        "Name": "单价",
                        "Value": "",
                        "Row": -1
                    },
                    {
                        "Name": "备注",
                        "Value": "",
                        "Row": -1
                    },
                    {
                        "Name": "单位",
                        "Value": "",
                        "Row": -1
                    },
                    {
                        "Name": "数量",
                        "Value": "",
                        "Row": -1
                    },
                    {
                        "Name": "规格型号",
                        "Value": "",
                        "Row": -1
                    },
                    {
                        "Name": "是否代开",
                        "Value": "",
                        "Row": -1
                    },
                    {
                        "Name": "成品油标志",
                        "Value": "",
                        "Row": -1
                    },
                    {
                        "Name": "服务类型",
                        "Value": "",
                        "Row": -1
                    },
                    {
                        "Name": "通行费标志",
                        "Value": "",
                        "Row": -1
                    },
                    {
                        "Name": "车船税",
                        "Value": "",
                        "Row": -1
                    },
                    {
                        "Name": "车牌号",
                        "Value": "",
                        "Row": -1
                    },
                    {
                        "Name": "类型",
                        "Value": "",
                        "Row": -1
                    },
                    {
                        "Name": "通行日期起",
                        "Value": "",
                        "Row": -1
                    },
                    {
                        "Name": "通行日期止",
                        "Value": "",
                        "Row": -1
                    }
                ]
            }
        ],
        "RequestId": "3a850dbc-2de1-4dfb-9ecd-7ae57f2fe666"
    }
}
```

