**Example 1: 查询订单信息**

查询订单信息

Input: 

```
tccli postgres DescribeOrders --cli-unfold-argument  \
    --DealNames 20180615110033
```

Output: 
```
{
    "Response": {
        "Deals": [
            {
                "Count": 1,
                "OwnerUin": "909619400",
                "DBInstanceIdSet": [
                    "postgres-2uepfuz1"
                ],
                "PayMode": 1,
                "FlowId": 36,
                "DealName": "20180615110033"
            }
        ],
        "TotalCount": 1,
        "RequestId": "08fdf411-5d39-44f2-8e1d-a58ee60b237d"
    }
}
```

