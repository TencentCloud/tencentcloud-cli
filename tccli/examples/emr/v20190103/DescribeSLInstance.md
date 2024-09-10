**Example 1: Lite HBase 查询实例信息**

Lite HBase 查询实例信息

Input: 

```
tccli emr DescribeSLInstance --cli-unfold-argument  \
    --InstanceId emr-3o9tms4i
```

Output: 
```
{
    "Response": {
        "DiskSize": 100,
        "DiskType": "性能云存储",
        "InstanceName": "sl-haoyuhua-test-create",
        "NodeType": "4C16G",
        "PayMode": 0,
        "RequestId": "a316989f-9316-4205-a2a3-64ab841aee14",
        "ZoneSettings": [
            {
                "NodeNum": 1,
                "VPCSettings": {
                    "SubnetId": "subnet-5bhc4kly",
                    "VpcId": "vpc-dcfhrh73"
                },
                "Zone": "ap-guangzhou-2"
            },
            {
                "NodeNum": 1,
                "VPCSettings": {
                    "SubnetId": "subnet-5bhc4kly",
                    "VpcId": "vpc-dcfhrh73"
                },
                "Zone": "ap-guangzhou-2"
            },
            {
                "NodeNum": 1,
                "VPCSettings": {
                    "SubnetId": "subnet-5bhc4kly",
                    "VpcId": "vpc-dcfhrh73"
                },
                "Zone": "ap-guangzhou-2"
            }
        ]
    }
}
```

