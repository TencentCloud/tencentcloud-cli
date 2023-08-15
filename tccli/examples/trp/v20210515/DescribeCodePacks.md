**Example 1: 查询码包列表**



Input: 

```
tccli trp DescribeCodePacks --cli-unfold-argument  \
    --Keyword  \
    --PageSize 10 \
    --PageNumber 1
```

Output: 
```
{
    "Response": {
        "CodePacks": [
            {
                "PackId": "abc",
                "CorpId": 0,
                "MerchantId": "abc",
                "CreateTime": "abc",
                "UpdateTime": "abc",
                "Status": "abc",
                "Log": "abc",
                "CreateUser": "abc",
                "Amount": 0,
                "CodeLength": 0,
                "CodeType": "abc",
                "Cipher": 0,
                "TextUrl": "abc",
                "PackUrl": "abc",
                "MerchantName": "abc",
                "RuleType": 0,
                "CustomId": "abc",
                "PackType": 0,
                "PackLevel": 1,
                "PackSpec": [
                    {
                        "Level": 1,
                        "Rate": 1,
                        "Amount": 1,
                        "CustomId": "abc",
                        "CodeParts": [
                            {
                                "Name": "abc",
                                "Type": "abc",
                                "Value": "abc",
                                "Length": 1,
                                "Ext": "abc"
                            }
                        ]
                    }
                ]
            }
        ],
        "TotalCount": 1,
        "RequestId": "abc"
    }
}
```

