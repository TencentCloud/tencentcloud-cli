**Example 1: 解析SDK获取到的证件NFC数据**

解析SDK获取到的证件NFC数据。

Input: 

```
tccli faceid ParseNfcData --cli-unfold-argument  \
    --ReqId eyJyZXFJZCI6IjEyMzEiLCJkZXZpY2VJZCI6IjQ1NiJ9
```

Output: 
```
{
    "Response": {
        "Address": "北京市东城区景山前街4号紫禁城敬事房",
        "BeginTime": "20170405",
        "BirthDate": "19890604",
        "CheckMRTD": "",
        "EnName": "",
        "EndTime": "20260704",
        "IdNum": "11204416541220243X",
        "IdType": "",
        "ImageA": "/9j/4AAQSkZJRg.....s97n//2Q==",
        "ImageB": "/9j/4AAQSk...mA7pvm5g==",
        "Name": "韦小宝",
        "Nation": "汉",
        "Nationality": "",
        "OtherIdNum": "",
        "PersonalNumber": "",
        "Picture": "Qk3OlwAAAA...7+/v7+/pAA",
        "RequestId": "cdd7a769-d288-42a5-8e2e-6a5e5c9c08ae",
        "ResultCode": "0",
        "Sex": "男",
        "SigningOrganization": "北京市东城区分局",
        "ResultDescription": "首次查询成功"
    }
}
```

