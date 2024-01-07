**Example 1: CreatePlanForZone**

为站点创建套餐

Input: 

```
tccli teo CreatePlanForZone --cli-unfold-argument  \
    --ZoneId zone-25z65bfb4414 \
    --PlanType sta
```

Output: 
```
{
    "Response": {
        "RequestId": "a06f52e7-2aab-4510-b2c2-1065bfb4414c",
        "ResourceNames": [
            "plan_sta"
        ],
        "DealNames": [
            "2022080135400110011001"
        ]
    }
}
```

