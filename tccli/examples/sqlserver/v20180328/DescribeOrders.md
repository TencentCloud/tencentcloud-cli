**Example 1: 查询订单**



Input: 

```
tccli sqlserver DescribeOrders --cli-unfold-argument  \
    --DealNames 201806271245
```

Output: 
```
{
    "Response": {
        "RequestId": "4be5990d-a4b5-49dc-b2b4-e713b6aa7ba3",
        "TotalCount": 10,
        "Deals": [
            {
                "DealName": "201806271765",
                "OwnerUin": "3374998458",
                "Count": 1,
                "FlowId": 3456,
                "InstanceIdSet": [
                    "mssql-k8vodfsw"
                ],
                "InstanceChargeType": "POST"
            }
        ]
    }
}
```

