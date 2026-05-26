**Example 1: 拉取NFC结果**



Input: 

```
tccli faceid GetWxNFCResult --cli-unfold-argument  \
    --NFCToken d102c9c8-5423-11f1-97f9-52540044344e
```

Output: 
```
{
    "Response": {
        "Address": "福建省**市*************区*幢*单元***室",
        "BeginTime": "",
        "BirthDate": "",
        "CheckMRTD": "",
        "EnName": "ZHAN***ZHEN",
        "EndTime": "",
        "IdCardBackImg": "",
        "IdCardFrontImg": "",
        "IdNum": "350481***111140011",
        "IdType": "",
        "Name": "张*",
        "Nation": "",
        "Nationality": "",
        "OtherIdNum": "",
        "PersonalNumber": "",
        "Picture": "",
        "ResultCode": "-1",
        "Sex": "",
        "SigningOrganization": "永安市***",
        "RequestId": "096513c7-1ee5-4620-a36b-9f5101cd2737"
    }
}
```

