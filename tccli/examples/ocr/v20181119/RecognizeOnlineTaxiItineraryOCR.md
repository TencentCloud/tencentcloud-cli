**Example 1: 网约车行程单识别示例代码**

网约车行程单识别示例代码

Input: 

```
tccli ocr RecognizeOnlineTaxiItineraryOCR --cli-unfold-argument  \
    --ImageUrl https://xx/a.jpg
```

Output: 
```
{
    "Response": {
        "OnlineTaxiItineraryInfos": [
            {
                "Name": "行程单分类",
                "Row": -1,
                "Value": "乐橙网约车-行程单"
            },
            {
                "Name": "申请日期",
                "Row": -1,
                "Value": "2020年09月04日"
            },
            {
                "Name": "行程开始日期",
                "Row": -1,
                "Value": "2020年09月01日"
            },
            {
                "Name": "行程结束日期",
                "Row": -1,
                "Value": "2020年09月01日"
            },
            {
                "Name": "手机号",
                "Row": -1,
                "Value": "13447844750"
            },
            {
                "Name": "车型",
                "Row": 0,
                "Value": "快车"
            },
            {
                "Name": "城市",
                "Row": 0,
                "Value": "深圳"
            },
            {
                "Name": "上车时间",
                "Row": 0,
                "Value": "09-0107:57周二"
            },
            {
                "Name": "起点",
                "Row": 0,
                "Value": "碧海湾"
            },
            {
                "Name": "终点",
                "Row": 0,
                "Value": "大鹏所城"
            },
            {
                "Name": "里程",
                "Row": 0,
                "Value": "89.6公里"
            },
            {
                "Name": "金额",
                "Row": 0,
                "Value": "324元"
            }
        ],
        "RequestId": "167d28e1-a0da-450c-9368-07ef35634ab6"
    }
}
```

