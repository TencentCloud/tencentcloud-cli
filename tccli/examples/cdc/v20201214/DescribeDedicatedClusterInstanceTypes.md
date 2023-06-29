**Example 1: 查询专用集群支持的实例规格列表**

查询专用集群支持的实例规格列表

Input: 

```
tccli cdc DescribeDedicatedClusterInstanceTypes --cli-unfold-argument  \
    --DedicatedClusterId cluster-gbo27yc4
```

Output: 
```
{
    "Response": {
        "DedicatedClusterInstanceTypeSet": [
            {
                "Zone": "ap-guangzhou-2",
                "InstanceType": "S1.SMALL1",
                "NetworkCard": 0,
                "Cpu": 1,
                "Memory": 1,
                "InstanceFamily": "S1",
                "TypeName": "Standard S1",
                "StorageBlockAmount": 0,
                "InstanceBandwidth": 0,
                "InstancePps": 0,
                "CpuType": "",
                "Gpu": 0,
                "Fpga": 0,
                "Remark": "",
                "Status": "SOLD_OUT"
            },
            {
                "Zone": "ap-guangzhou-2",
                "InstanceType": "S3.SMALL1",
                "NetworkCard": 0,
                "Cpu": 1,
                "Memory": 1,
                "InstanceFamily": "S3",
                "TypeName": "Standard S3",
                "StorageBlockAmount": 0,
                "InstanceBandwidth": 0,
                "InstancePps": 0,
                "CpuType": "",
                "Gpu": 0,
                "Fpga": 0,
                "Remark": "",
                "Status": "SOLD_OUT"
            }
        ],
        "RequestId": "90ddf8cf-168b-4175-99f0-28858e90634a"
    }
}
```

