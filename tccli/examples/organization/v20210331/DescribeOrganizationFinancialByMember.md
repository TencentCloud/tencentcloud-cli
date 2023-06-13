**Example 1: 按成员维度获取企业财务信息**

按成员维度获取企业财务信息

Input: 

```
tccli organization DescribeOrganizationFinancialByMember --cli-unfold-argument  \
    --Month 2021-04
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "MemberName": "test2",
                "MemberUin": 111111111111,
                "TotalCost": 99,
                "Ratio": "79.5"
            },
            {
                "MemberName": "test1",
                "MemberUin": 222222222222,
                "TotalCost": 12.22,
                "Ratio": "20.5"
            }
        ],
        "RequestId": "dd729295-1586-4395-9286-598dadccc88d",
        "TotalCost": 1002.1,
        "Total": 2
    }
}
```

