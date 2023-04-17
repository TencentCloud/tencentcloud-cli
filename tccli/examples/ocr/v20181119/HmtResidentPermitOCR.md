**Example 1: 港澳台居住证识别示例代码1**

港澳台居住证识别示例代码1

Input: 

```
tccli ocr HmtResidentPermitOCR --cli-unfold-argument  \
    --ImageUrl https://xx/a.jpg \
    --CardSide FRONT
```

Output: 
```
{
    "Response": {
        "Name": "李优优",
        "Sex": "女",
        "Birth": "1997/6/2",
        "Address": "上海市徐汇区古美路1528号A1栋腾讯优图1号",
        "IdCardNo": "830000199706020042",
        "CardType": 0,
        "ValidDate": "",
        "Authority": "",
        "VisaNum": "0",
        "PassNo": "000",
        "RequestId": "f72e7048-f1e0-42f3-b0bf-f8730d48bb5c"
    }
}
```

**Example 2: 港澳台居住证识别示例代码2**

港澳台居住证识别示例代码2

Input: 

```
tccli ocr HmtResidentPermitOCR --cli-unfold-argument  \
    --ImageUrl https://xx/a.jpg
```

Output: 
```
{
    "Response": {
        "Name": "",
        "Sex": "",
        "Birth": "",
        "Address": "",
        "IdCardNo": "",
        "CardType": 1,
        "ValidDate": "2018.09.06-2023.09.06",
        "Authority": "合肥市公安局高新分局",
        "VisaNum": "0",
        "PassNo": "000",
        "RequestId": "182abb0c-b0bd-403a-ab11-3dba21ae89d0"
    }
}
```

