**Example 1: 查询安心计划二维码列表**



Input: 

```
tccli trp DescribePlanQRCodes --cli-unfold-argument  \
    --PlanId 67087 \
    --StartTime 2023-10-10 00:00:00 \
    --EndTime 2023-10-10 23:59:59 \
    --PageNo 1 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "Ret": 0,
        "Total": 1,
        "Data": [
            {
                "Url": "xxx",
                "Status": 1
            }
        ],
        "RequestId": "abc"
    }
}
```

