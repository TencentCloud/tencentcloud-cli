**Example 1: 查询预留实例机型配置**

查询预留实例机型配置

Input: 

```
tccli cvm DescribeReservedInstancesConfigInfos --cli-unfold-argument  \
    --Filters.0.Name zone \
    --Filters.0.Values ap-guangzhou-1
```

Output: 
```
{
    "Response": {
        "ReservedInstanceConfigInfos": [
            {
                "Type": "C",
                "TypeName": "计算型",
                "Order": 0,
                "InstanceFamilies": [
                    {
                        "InstanceFamily": "abc",
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
                                "MaxBandwidth": 0,
                                "Frequency": "2.5",
                                "CpuModelName": "Intel Xeon Skylake 6146",
                                "Pps": 60,
                                "Externals": {
                                    "ReleaseAddress": true,
                                    "UnsupportNetworks": [],
                                    "StorageBlockAttr": {
                                        "Type": "",
                                        "MinSize": 0,
                                        "MaxSize": 0
                                    }
                                },
                                "Remark": "",
                                "Prices": [
                                    {
                                        "ReservedInstancesOfferingId": "d81353d7-fe7d-43d0-a361-fb5633a9a7e5",
                                        "OfferingType": "No Upfront",
                                        "FixedPrice": 0,
                                        "UsagePrice": 2.99,
                                        "Duration": 1,
                                        "Zone": "ap-guangzhou-1",
                                        "ProductDescription": ""
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

