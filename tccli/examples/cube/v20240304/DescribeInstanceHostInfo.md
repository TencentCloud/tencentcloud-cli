**Example 1: 获取实例所在裸金属信息**

获取实例所在裸金属信息

Input: 

```
tccli cube DescribeInstanceHostInfo --cli-unfold-argument  \
    --InstanceId ins-e4c2c5be
```

Output: 
```
{
    "Response": {
        "CPU": 256,
        "DeviceClass": "VSBMSA_3",
        "DeviceId": 267634210,
        "HostIp": "30.64.217.68",
        "InstanceFamily": "BMSA3",
        "InstanceId": "ins-e4c2c5be",
        "InstanceState": "RUNNING",
        "InstanceType": "BMSA3.64XLARGE512",
        "InstanceUuid": "11077e5-be1f-42c6-bfb8-d766b5c85618",
        "RequestId": "76ae6914-f51d-43af-93c6-bc02e1670a7b",
        "VirtualCpu": 25600,
        "VirtualNodeQuota": [
            12800,
            12800
        ]
    }
}
```

