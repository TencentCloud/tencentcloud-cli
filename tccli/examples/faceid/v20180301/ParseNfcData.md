**Example 1: success**



Input: 

```
tccli faceid ParseNfcData --cli-unfold-argument  \
    --ReqId eyJyZXFJZCI6IjEyMzEiLCJkZXZpY2VJZCI6IjQ1NiJ9
```

Output: 
```
{
    "Response": {
        "Address": "北京**********",
        "BeginTime": "20******",
        "BirthDate": "19******",
        "CheckMRTD": "",
        "EnName": "",
        "EndTime": "20******",
        "IdNum": "3****************6",
        "IdType": "",
        "ImageA": "/9j/4A",
        "ImageB": "/9j/4A",
        "Name": "*四",
        "Nation": "汉",
        "Nationality": "",
        "OtherIdNum": "",
        "PersonalNumber": "",
        "Picture": "iVBORw",
        "RequestId": "cdd7a769-d288-42a5-8e2e-6a5e5c9c08ae",
        "ResultCode": "0",
        "Sex": "男",
        "SigningOrganization": "*******阳分局",
        "ResultDescription": "首次查询成功"
    }
}
```

