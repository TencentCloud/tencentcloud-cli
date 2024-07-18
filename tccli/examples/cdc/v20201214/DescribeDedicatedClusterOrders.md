**Example 1: 查询专用集群订单列表**

查询专用集群订单列表

Input: 

```
tccli cdc DescribeDedicatedClusterOrders --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "DedicatedClusterOrderSet": [
            {
                "DedicatedClusterId": "abc",
                "DedicatedClusterTypeId": "abc",
                "SupportedStorageType": [
                    "abc"
                ],
                "SupportedUplinkSpeed": [
                    0
                ],
                "SupportedInstanceFamily": [
                    "abc"
                ],
                "Weight": 0,
                "PowerDraw": 0,
                "OrderStatus": "abc",
                "CreateTime": "2020-09-22T00:00:00+00:00",
                "DedicatedClusterOrderId": "abc",
                "Action": "abc",
                "DedicatedClusterOrderItems": [
                    {
                        "DedicatedClusterTypeId": "abc",
                        "SupportedStorageType": [
                            "abc"
                        ],
                        "SupportedUplinkSpeed": [
                            0
                        ],
                        "SupportedInstanceFamily": [
                            "abc"
                        ],
                        "Weight": 0,
                        "PowerDraw": 0,
                        "SubOrderStatus": "abc",
                        "CreateTime": "2020-09-22T00:00:00+00:00",
                        "SubOrderId": "abc",
                        "Count": 0,
                        "Name": "abc",
                        "Description": "abc",
                        "TotalCpu": 0,
                        "TotalMem": 0,
                        "TotalGpu": 0,
                        "TypeName": "abc",
                        "ComputeFormat": "abc",
                        "TypeFamily": "abc",
                        "SubOrderPayStatus": 0
                    }
                ],
                "Cpu": 0,
                "Mem": 0,
                "Gpu": 0,
                "PayStatus": 0,
                "PayType": "abc",
                "TimeUnit": "abc",
                "TimeSpan": 0,
                "OrderType": "abc",
                "CheckStatus": "abc",
                "DeliverExpectTime": "abc",
                "DeliverFinishTime": "abc",
                "CheckExpectTime": "abc",
                "CheckFinishTime": "abc",
                "OrderSLA": "abc",
                "OrderPayPlan": "abc"
            }
        ],
        "TotalCount": 0,
        "RequestId": "abc"
    }
}
```

