**Example 1: 获取联系人信息**



Input: 

```
tccli chc DescribeWorkOrderPersonnelCollectList --cli-unfold-argument  \
    --Offset 2 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "PersonnelSet": [
            {
                "Company": "****科技有限公司",
                "IDCardNumber": "******************",
                "IDCardType": "IDENTITY_CARD",
                "LanguageType": "CHINESE",
                "Name": "卡夫卡",
                "TelNumber": "1**********"
            }
        ],
        "TotalCount": 51,
        "RequestId": "70695c72-bff9-4ca8-8722-74b17804d396"
    }
}
```

