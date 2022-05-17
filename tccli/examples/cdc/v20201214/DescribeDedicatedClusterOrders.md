**Example 1: 查询专用集群订单列表**



Input: 

```
tccli cdc DescribeDedicatedClusterOrders --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 4,
        "DedicatedClusterOrderSet": [
            {
                "DedicatedClusterTypeId": "xx",
                "PowerDraw": 2000.8,
                "Weight": 3000,
                "Mem": 0,
                "DedicatedClusterOrderItems": [
                    {
                        "Count": 0,
                        "DedicatedClusterTypeId": "xx",
                        "PowerDraw": 0.0,
                        "Name": "xx",
                        "Weight": 0,
                        "TotalMem": 0,
                        "TotalGpu": 0,
                        "TotalCpu": 0,
                        "SupportedStorageType": [
                            "xx"
                        ],
                        "ComputeFormat": "xx",
                        "TypeName": "xx",
                        "SubOrderStatus": "xx",
                        "SubOrderId": "xx",
                        "SupportedInstanceFamily": [
                            "xx"
                        ],
                        "SupportedUplinkSpeed": [
                            0
                        ],
                        "CreateTime": "2020-09-22T00:00:00+00:00",
                        "Description": "xx"
                    }
                ],
                "SupportedStorageType": [
                    "xx"
                ],
                "DedicatedClusterOrderId": "xx",
                "Action": "xx",
                "OrderStatus": "xx",
                "PayStatus": 0,
                "SupportedInstanceFamily": [
                    "S5"
                ],
                "Gpu": 0,
                "SupportedUplinkSpeed": [
                    40,
                    100
                ],
                "CreateTime": "2020-09-22T00:00:00+00:00",
                "Cpu": 0,
                "DedicatedClusterId": "xx"
            },
            {
                "DedicatedClusterTypeId": "xx",
                "PowerDraw": 4156.7,
                "Weight": 3273,
                "Mem": 0,
                "SupportedStorageType": [
                    "xx"
                ],
                "DedicatedClusterOrderId": "xx",
                "SupportedInstanceFamily": [
                    "S1",
                    "S5"
                ],
                "Cpu": 0,
                "OrderStatus": "xx",
                "Gpu": 0,
                "Action": "xx",
                "PayStatus": 0,
                "SupportedUplinkSpeed": [
                    13,
                    100
                ],
                "CreateTime": "2020-09-22T00:00:00+00:00",
                "DedicatedClusterOrderItems": [
                    {
                        "Count": 0,
                        "DedicatedClusterTypeId": "xx",
                        "PowerDraw": 0.0,
                        "Name": "xx",
                        "Weight": 0,
                        "TotalGpu": 0,
                        "TotalCpu": 0,
                        "SupportedStorageType": [
                            "xx"
                        ],
                        "ComputeFormat": "xx",
                        "TypeName": "xx",
                        "SubOrderStatus": "xx",
                        "SubOrderId": "xx",
                        "SupportedInstanceFamily": [
                            "xx"
                        ],
                        "Description": "xx",
                        "SupportedUplinkSpeed": [
                            0
                        ],
                        "CreateTime": "2020-09-22T00:00:00+00:00",
                        "TotalMem": 0
                    }
                ],
                "DedicatedClusterId": "xx"
            },
            {
                "DedicatedClusterTypeId": "xx",
                "PowerDraw": 3829.1,
                "Weight": 3724,
                "Mem": 0,
                "SupportedStorageType": [
                    "xx"
                ],
                "DedicatedClusterOrderId": "xx",
                "SupportedInstanceFamily": [
                    "S3"
                ],
                "Cpu": 0,
                "OrderStatus": "xx",
                "Gpu": 0,
                "Action": "xx",
                "PayStatus": 0,
                "SupportedUplinkSpeed": [
                    10,
                    40
                ],
                "CreateTime": "2020-09-22T00:00:00+00:00",
                "DedicatedClusterOrderItems": [
                    {
                        "Count": 0,
                        "DedicatedClusterTypeId": "xx",
                        "PowerDraw": 0.0,
                        "Name": "xx",
                        "Weight": 0,
                        "TotalGpu": 0,
                        "TotalCpu": 0,
                        "SupportedStorageType": [
                            "xx"
                        ],
                        "ComputeFormat": "xx",
                        "TypeName": "xx",
                        "SubOrderStatus": "xx",
                        "SubOrderId": "xx",
                        "SupportedInstanceFamily": [
                            "xx"
                        ],
                        "Description": "xx",
                        "SupportedUplinkSpeed": [
                            0
                        ],
                        "CreateTime": "2020-09-22T00:00:00+00:00",
                        "TotalMem": 0
                    }
                ],
                "DedicatedClusterId": "xx"
            },
            {
                "DedicatedClusterTypeId": "xx",
                "PowerDraw": 3829.1,
                "Weight": 3724,
                "Mem": 0,
                "SupportedStorageType": [
                    "xx"
                ],
                "DedicatedClusterOrderId": "xx",
                "SupportedInstanceFamily": [
                    "xx"
                ],
                "Cpu": 0,
                "OrderStatus": "xx",
                "Gpu": 0,
                "Action": "xx",
                "PayStatus": 0,
                "SupportedUplinkSpeed": [
                    10,
                    40
                ],
                "CreateTime": "2020-09-22T00:00:00+00:00",
                "DedicatedClusterOrderItems": [
                    {
                        "Count": 0,
                        "DedicatedClusterTypeId": "xx",
                        "PowerDraw": 0.0,
                        "Name": "xx",
                        "Weight": 0,
                        "TotalGpu": 0,
                        "TotalCpu": 0,
                        "SupportedStorageType": [
                            "xx"
                        ],
                        "ComputeFormat": "xx",
                        "TypeName": "xx",
                        "SubOrderStatus": "xx",
                        "SubOrderId": "xx",
                        "SupportedInstanceFamily": [
                            "xx"
                        ],
                        "Description": "xx",
                        "SupportedUplinkSpeed": [
                            0
                        ],
                        "CreateTime": "2020-09-22T00:00:00+00:00",
                        "TotalMem": 0
                    }
                ],
                "DedicatedClusterId": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

