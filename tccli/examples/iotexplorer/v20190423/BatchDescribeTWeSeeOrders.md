**Example 1: 批量查询 TWeSee 订单**

同时按订单 ID 和自定义订单 ID 批量查询订单状态。

Input: 

```
tccli iotexplorer BatchDescribeTWeSeeOrders --cli-unfold-argument  \
    --Entries.0.OrderId 2026042**********584511 \
    --Entries.1.CustomOrderId custom-order-002
```

Output: 
```
{
    "Response": {
        "Results": [
            {
                "OrderId": "2026042**********584511",
                "CustomOrderId": "custom-order-001",
                "Status": "DELIVERED",
                "Price": "1200",
                "Currency": "CNY",
                "ResourceId": "twesee-753yd29x30********jqww1"
            },
            {
                "OrderId": "",
                "CustomOrderId": "custom-order-002",
                "Status": "QUERY_FAILED",
                "ErrorCode": "FailedOperation.CustomOrderIdNotExist",
                "ErrorMessage": "自定义订单 ID 不存在"
            }
        ],
        "RequestId": "0d350a07-0fc9-455c-98c8-0946d721dc1a"
    }
}
```

