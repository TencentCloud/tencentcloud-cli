**Example 1: 查询专用集群订单列表**

查询专用集群订单列表

Input: 

```
tccli cdc DescribeDedicatedClusterOrders --cli-unfold-argument  \
    --DedicatedClusterIds cluster-262n63e8 \
    --Offset 0 \
    --Limit 1 \
    --ActionType CREATE \
    --OrderTypes PUSH
```

Output: 
```
{
    "Response": {
        "DedicatedClusterOrderSet": [
            {
                "Action": "CREATE",
                "CheckExpectTime": "0000-00-00 00:00:00",
                "CheckFinishTime": "0000-00-00 00:00:00",
                "CheckStatus": "DELIVERING",
                "Cpu": 0,
                "CreateTime": "2024-09-22T00:00:00+00:00",
                "DedicatedClusterId": "cluster-262n63e8",
                "DedicatedClusterOrderId": "ord-rd0ty398",
                "DedicatedClusterOrderItems": [
                    {
                        "ComputeFormat": "1 SA5t.60XLARGE1076",
                        "Count": 1,
                        "CreateTime": "2024-09-22T00:00:00+00:00",
                        "DedicatedClusterTypeId": "dctype-00100001",
                        "Description": "基础底座",
                        "Name": "基础底座",
                        "PowerDraw": 0,
                        "SubOrderId": "sord-e3t9jkm2",
                        "SubOrderPayStatus": 0,
                        "SubOrderStatus": "PENDING",
                        "SupportedInstanceFamily": [],
                        "SupportedStorageType": [],
                        "SupportedUplinkSpeed": [
                            10,
                            25,
                            40,
                            100
                        ],
                        "TotalCpu": 0,
                        "TotalGpu": 0,
                        "TotalMem": 0,
                        "TypeFamily": "CUSTOM",
                        "TypeName": "BASE_EQUIPMENT.BASE_FOUNDATION",
                        "Weight": 0
                    }
                ],
                "DedicatedClusterTypeId": "None",
                "DeliverExpectTime": "0000-00-00 00:00:00",
                "DeliverFinishTime": "0000-00-00 00:00:00",
                "Gpu": 0,
                "Mem": 0,
                "OrderPayPlan": null,
                "OrderSLA": null,
                "OrderStatus": "PENDING",
                "OrderType": "PUSH",
                "PayStatus": 0,
                "PayType": "ONEOFF",
                "PowerDraw": 0,
                "SupportedInstanceFamily": [
                    "None"
                ],
                "SupportedStorageType": [
                    "None"
                ],
                "SupportedUplinkSpeed": [
                    -1
                ],
                "TimeSpan": 3,
                "TimeUnit": "YEAR",
                "Weight": 0
            }
        ],
        "RequestId": "3da146fc-0136-4386-b632-9dbef7f06431",
        "TotalCount": 30
    }
}
```

