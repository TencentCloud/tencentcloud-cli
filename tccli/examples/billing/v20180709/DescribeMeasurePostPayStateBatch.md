**Example 1: 批量查询计量后付费按量计费策略**

无

Input: 

```
tccli billing DescribeMeasurePostPayStateBatch --cli-unfold-argument  \
    --Para.0.ProductCode p_bsp \
    --Para.0.SubscriptionId bsp100570
```

Output: 
```
{
    "Response": {
        "Data": {
            "Data": [
                {
                    "ProductCode": "p_bsp",
                    "State": 1,
                    "SubProductCode": "",
                    "SubscriptionId": "bsp100570"
                }
            ]
        },
        "RequestId": "16c87052-35a2-4028-b400-a74726a18521"
    }
}
```

