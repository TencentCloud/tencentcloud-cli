**Example 1: 添加企业架构资产**



Input: 

```
tccli ctem CreateEnterprise --cli-unfold-argument  \
    --Name 测试 \
    --CreditCode test \
    --Status 存续 \
    --RegisteredCapital 100元 \
    --ShareholdingRatio 100% \
    --LegalPerson 张三 \
    --Type 软件 \
    --Industry 软件 \
    --CustomerId 100068
```

Output: 
```
{
    "Response": {
        "Id": 2077,
        "RequestId": "fd673644-6c6b-40c5-ba8c-f339a56a49e5"
    }
}
```

