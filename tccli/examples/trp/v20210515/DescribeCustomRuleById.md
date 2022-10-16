**Example 1: 查自定义码规则**



Input: 

```
tccli trp DescribeCustomRuleById --cli-unfold-argument  \
    --CustomId gss06ki67crv
```

Output: 
```
{
    "Response": {
        "CustomRule": {
            "CustomId": "gss06ki67crv",
            "Name": "demo2",
            "CorpId": 10000,
            "MerchantId": "6b1tvtwfve3n",
            "CodeLength": 16,
            "Status": 1,
            "CodeParts": [],
            "CreateTime": "2022-09-19T11:46:53.000Z",
            "UpdateTime": "2022-09-19T11:48:06.000Z"
        },
        "RequestId": "14b0a199-42cc-405c-984a-b5bcffe56009"
    }
}
```

