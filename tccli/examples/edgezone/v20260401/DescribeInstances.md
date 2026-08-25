**Example 1: 按可用区和状态筛选实例**

查询广州一区运行中的实例列表

Input: 

```
tccli edgezone DescribeInstances --cli-unfold-argument  \
    --Zone ap-guangzhou-1 \
    --InstanceStatus running \
    --Offset 0 \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "InstanceSet": [
            {
                "InstanceId": "epm-efgh5678",
                "InstanceName": "web-server-01",
                "MachineId": "srv-efgh5678",
                "InstanceType": "BM.S5.LARGE8",
                "Zone": "ap-guangzhou-1",
                "ImageId": "img-ubuntu-20.04",
                "VersionNumber": "20.04",
                "InstanceStatus": "running",
                "OperateStatus": "normal",
                "PrivateNetworkId": "net-private-002",
                "PrivateIp": "10.0.0.2",
                "PrivateIpV6": "",
                "PublicNetworkId": "net-public-002",
                "PublicIp": "203.0.113.20",
                "PublicIpV6": "",
                "CreatedTime": "2026-02-15T14:30:00Z"
            }
        ],
        "TotalCount": 1,
        "RequestId": "b5d7f3a2-c418-4b9e-9c72-4a1e6d3f8b90"
    }
}
```

**Example 2: 查询实例列表**

按实例ID查询实例列表

Input: 

```
tccli edgezone DescribeInstances --cli-unfold-argument  \
    --InstanceIds epm-abcd1234 \
    --Offset 0 \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "InstanceSet": [
            {
                "InstanceId": "epm-abcd1234",
                "InstanceName": "my-epm-instance",
                "MachineId": "srv-abcd1234",
                "InstanceType": "BM.S5.LARGE8",
                "Zone": "ap-guangzhou-1",
                "ImageId": "img-centos-7.9",
                "VersionNumber": "7.9.2009",
                "InstanceStatus": "running",
                "OperateStatus": "normal",
                "PrivateNetworkId": "net-private-001",
                "PrivateIp": "10.0.0.1",
                "PrivateIpV6": "fd00::1",
                "PublicNetworkId": "net-public-001",
                "PublicIp": "203.0.113.10",
                "PublicIpV6": "2001:db8::1",
                "CreatedTime": "2026-01-13T10:00:00Z"
            }
        ],
        "TotalCount": 1,
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

