**Example 1: 查余额用例返回验证**

查余额用例返回验证

Input: 

```
tccli billing DescribeOrgMemberAccountBalance --cli-unfold-argument  \
    --MemberUins 700001941608
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "BasicCreditAmount": 0,
                "CashAccountBalance": 36365911,
                "CreditAmount": 0,
                "IsCreditAccount": false,
                "MemberName": "kleinerwang_test",
                "MemberUin": "700001941608",
                "OweAmount": 0,
                "RealBalance": 36365911,
                "TempCredit": 0
            }
        ],
        "PageNumber": 1,
        "PageSize": 1,
        "TotalCount": 1,
        "RequestId": "241b92ef-b68e-4827-ae15-5ef7f3bd4009"
    }
}
```

