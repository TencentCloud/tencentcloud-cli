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
                "DedicatedClusterId": "xx",
                "DedicatedClusterTypeId": "xx",
                "SupportedStorageType": [
                    "xx"
                ],
                "SupportedUplinkSpeed": [
                    0
                ],
                "SupportedInstanceFamily": [
                    "xx"
                ],
                "Weight": 0,
                "PowerDraw": 0,
                "OrderStatus": "xx",
                "CreateTime": "2020-09-22T00:00:00+00:00",
                "DedicatedClusterOrderId": "xx",
                "Action": "xx",
                "DedicatedClusterOrderItems": [
                    {
                        "DedicatedClusterTypeId": "xx",
                        "SupportedStorageType": [
                            "xx"
                        ],
                        "SupportedUplinkSpeed": [
                            0
                        ],
                        "SupportedInstanceFamily": [
                            "xx"
                        ],
                        "Weight": 0,
                        "PowerDraw": 0,
                        "SubOrderStatus": "xx",
                        "CreateTime": "2020-09-22T00:00:00+00:00",
                        "SubOrderId": "xx",
                        "Count": 0,
                        "Name": "xx",
                        "Description": "xx",
                        "TotalCpu": 0,
                        "TotalMem": 0,
                        "TotalGpu": 0,
                        "TypeName": "xx",
                        "ComputeFormat": "xx",
                        "TypeFamily": "xx",
                        "SubOrderPayStatus": 0
                    }
                ],
                "Cpu": 0,
                "Mem": 0,
                "Gpu": 0,
                "PayStatus": 0,
                "PayType": "xx",
                "TimeUnit": "xx",
                "TimeSpan": 0,
                "OrderType": "xx"
            }
        ],
        "TotalCount": 0,
        "RequestId": "xx"
    }
}
```

