**Example 1: 查询实例资源池预扣包列表**

查询实例资源池预扣包列表

Input: 

```
tccli cvm DescribeResourcePoolPacks --cli-unfold-argument  \
    --MaxResults 10
```

Output: 
```
{
    "Response": {
        "DedicatedResourcePackSet": [
            {
                "AutoPlacement": true,
                "AvailableCapacity": {
                    "Cpu": 28,
                    "Disk": 0,
                    "Gpu": 0,
                    "Memory": 56
                },
                "DedicatedResourcePackId": "rpp-2gyonkx7",
                "DedicatedResourcePackName": "",
                "EndTime": "2026-03-07T10:19:40Z",
                "HostIp": "28F18A615F13777FCD220D3D4AF9D956",
                "InstanceFamily": "S9",
                "InstanceType": "S9.8XLARGE64",
                "RackId": "1A2A88376C7181435588E9FA520CE151",
                "RenewFlag": "NOTIFY_AND_MANUAL_RENEW",
                "ResourcePoolPackType": "EXCLUSIVE",
                "StartTime": "2026-02-07T10:19:40Z",
                "Status": "ACTIVE",
                "SwitchId": "3A7F5B75F1B7E292920E7118FD652EFD",
                "TotalCapacity": {
                    "Cpu": 32,
                    "Disk": 0,
                    "Gpu": 0,
                    "Memory": 64
                },
                "Zone": "ap-guangzhou-7"
            }
        ],
        "RequestId": "ff3e17a5-592c-4391-83d7-904210e92e95"
    }
}
```

