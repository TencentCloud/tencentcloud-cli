**Example 1: 查询预留实例机型配置**



Input: 

```
tccli cvm DescribeReservedInstancesConfigInfos --cli-unfold-argument  \
    --Filters.0.Name zone\
    --Filters.0.Values ap-guangzhou-1\
    --Offset 0\
    --Limit 1
```

Output: 
```
{
    "Response": {
        "ReservedInstanceConfigInfos": [
            {
                "Type": "C",
                "TypeName": "计算型",
                "Order": 400,
                "InstanceFamilies": [
                    {
                        "InstanceFamily": "C3",
                        "TypeName": "计算型C3",
                        "Order": 402,
                        "InstanceTypes": [
                            {
                                "InstanceType": "C3.LARGE8",
                                "Cpu": 4,
                                "Memory": 8,
                                "Gpu": 0,
                                "Fpga": 0,
                                "StorageBlock": 0,
                                "NetworkCard": 0,
                                "MaxBandwidth": 2.5,
                                "Frequency": "3.2 GHz",
                                "CpuModelName": "Intel Xeon Skylake 6146",
                                "Pps": 60,
                                "Externals": {},
                                "Remark": "",
                                "Prices": [
                                    {
                                        "ReservedInstancesOfferingId": "de06832b-1961-4efd-a470-efee242812a8",
                                        "OfferingType": "All Upfront",
                                        "FixedPrice": 200.99,
                                        "UsagePrice": 0
                                    },
                                    {
                                        "ReservedInstancesOfferingId": "daa72710-c529-4ab3-afca-917e192ea49d",
                                        "OfferingType": "Partial Upfront",
                                        "FixedPrice": 100.99,
                                        "UsagePrice": 1.99
                                    },
                                    {
                                        "ReservedInstancesOfferingId": "d81353d7-fe7d-43d0-a361-fb5633a9a7e5",
                                        "OfferingType": "No Upfront",
                                        "FixedPrice": 0,
                                        "UsagePrice": 2.99
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }
        ],
        "RequestId": "87eccd3e-9e7a-4b42-be3a-87eccd3e"
    }
}
```

