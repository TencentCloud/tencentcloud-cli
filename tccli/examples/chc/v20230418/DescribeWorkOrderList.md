**Example 1: 查询工单列表**



Input: 

```
tccli chc DescribeWorkOrderList --cli-unfold-argument  \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "RequestId": "646158b8-b20d-4843-a31a-883b78246cd8",
        "TotalCount": 3247,
        "WorkOrderSet": [
            {
                "CreateTime": "2025-03-07 11:11:59",
                "Creator": "godwin2@test.com",
                "OrderStatus": "processing",
                "OrderType": "itCommon",
                "ServiceType": "serverCommon",
                "WorkOrderId": "ord-25030711115960582"
            }
        ]
    }
}
```

