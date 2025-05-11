**Example 1: 输入的订单未查询到结果**

订单号不存在或订单非当前伙伴的普通代客预付费订单

Input: 

```
tccli partners DescribeAgentDealsPriceDetailByDealName --cli-unfold-argument  \
    --DealCreatYear 2022 \
    --DealNames 20221129388001245619661 20221129388001245611101
```

Output: 
```
{
    "Response": {
        "DealList": [],
        "RequestId": "b70c7e34-9ea6-44a9-ba7c-40dc071b5116"
    }
}
```

**Example 2: 成功查询订单**

成功查询订单费用详情

Input: 

```
tccli partners DescribeAgentDealsPriceDetailByDealName --cli-unfold-argument  \
    --DealCreatYear 2025 \
    --DealNames 20250411030002731555371 20250411941002731407001
```

Output: 
```
{
    "Response": {
        "DealList": [
            {
                "DealName": "20250411030002731555371",
                "OwnerUin": "100000032030",
                "SubProductPriceDetail": [
                    {
                        "DiscountValue": 100,
                        "Name": "流量包",
                        "RealTotalCost": 9900,
                        "TotalCost": 9900
                    }
                ]
            },
            {
                "DealName": "20250411941002731407001",
                "OwnerUin": "700001111941",
                "SubProductPriceDetail": [
                    {
                        "DiscountValue": 100,
                        "Name": "带宽-按带宽计费",
                        "RealTotalCost": 0,
                        "TotalCost": 0
                    },
                    {
                        "DiscountValue": 87,
                        "Name": "内存-标准型S5",
                        "RealTotalCost": 3900,
                        "TotalCost": 4500
                    },
                    {
                        "DiscountValue": 87,
                        "Name": "CPU-标准型S5",
                        "RealTotalCost": 3900,
                        "TotalCost": 4500
                    },
                    {
                        "DiscountValue": 100,
                        "Name": "高效云系统盘",
                        "RealTotalCost": 3500,
                        "TotalCost": 3500
                    }
                ]
            }
        ],
        "RequestId": "73a3fa9b-6149-4165-aaf9-c6cc7f57e87c"
    }
}
```

