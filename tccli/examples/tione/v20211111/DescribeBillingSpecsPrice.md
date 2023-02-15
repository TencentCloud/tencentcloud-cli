**Example 1: 查询计费项价格 示例**

查询计费项价格

Input: 

```
tccli tione DescribeBillingSpecsPrice --cli-unfold-argument  \
    --SpecsParam.0.SpecName TI.S.MEDIUM.POST \
    --SpecsParam.0.SpecCount 1
```

Output: 
```
{
    "Response": {
        "SpecsPrice": [
            {
                "SpecName": "TI.S.MEDIUM.POST",
                "SpecCount": 1,
                "TotalCost": 70,
                "RealTotalCost": 70
            }
        ],
        "RequestId": "b7d048fe-e335-8b6e-a8d2-d68esk"
    }
}
```

