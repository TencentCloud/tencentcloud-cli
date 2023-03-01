**Example 1: 机票行程单识别示例代码**

机票行程单识别

Input: 

```
tccli ocr FlightInvoiceOCR --cli-unfold-argument  \
    --ImageUrl https://xx/a.jpg
```

Output: 
```
{
    "Response": {
        "FlightInvoiceInfos": [
            {
                "Name": "旅客姓名",
                "Value": "框吉周",
                "Row": -1
            },
            {
                "Name": "有效身份证件号码",
                "Value": "321023199412064545",
                "Row": -1
            },
            {
                "Name": "电子客票号码",
                "Value": "1234551410938",
                "Row": -1
            },
            {
                "Name": "验证码",
                "Value": "5003",
                "Row": -1
            },
            {
                "Name": "填开日期",
                "Value": "2019-04-22",
                "Row": -1
            },
            {
                "Name": "票价",
                "Value": "1160.00",
                "Row": -1
            },
            {
                "Name": "合计金额",
                "Value": "1340.00",
                "Row": -1
            }
        ],
        "RequestId": "fb410c56-5990-46d4-82f0-4619112afca9"
    }
}
```

