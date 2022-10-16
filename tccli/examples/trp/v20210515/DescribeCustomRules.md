**Example 1: 查自定义码规则列表**



Input: 

```
tccli trp DescribeCustomRules --cli-unfold-argument  \
    --Keyword  \
    --PageSize 10 \
    --PageNumber 1
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "CustomRules": [
            {
                "CustomId": "gss06ki67crv",
                "Name": "demo2",
                "CorpId": 10000,
                "MerchantId": "6b1tvtwfve3n",
                "CodeLength": 16,
                "Status": 1,
                "CodeParts": [],
                "CreateTime": "2022-09-19T11:46:53.000Z",
                "UpdateTime": "2022-09-19T11:48:06.000Z"
            }
        ],
        "RequestId": "xx"
    }
}
```

