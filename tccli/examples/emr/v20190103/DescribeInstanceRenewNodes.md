**Example 1: 预付费集群隔离后续费资源查询**

预付费集群隔离后续费资源查询

Input: 

```
tccli emr DescribeInstanceRenewNodes --cli-unfold-argument  \
    --InstanceId emr-6deluvd4
```

Output: 
```
{
    "Response": {
        "MetaInfo": [],
        "NodeList": [
            {
                "CpuNum": 8,
                "DiskSize": "100.00 GB",
                "EmrResourceId": "emr-123",
                "ExpireTime": "2024-10-23 21:00:26",
                "Flag": 1,
                "Ip": "0.0.0.0",
                "MemDesc": "16GB",
                "Spec": "CVM.S5",
                "StorageType": 5
            },
            {
                "CpuNum": 4,
                "DiskSize": "100.00 GB",
                "EmrResourceId": "emr-123",
                "ExpireTime": "2024-10-23 21:00:16",
                "Flag": 2,
                "Ip": "0.0.0.0",
                "MemDesc": "8GB",
                "Spec": "CVM.S5",
                "StorageType": 5
            },
            {
                "CpuNum": 4,
                "DiskSize": "100.00 GB",
                "EmrResourceId": "emr-123",
                "ExpireTime": "2024-10-23 21:00:21",
                "Flag": 2,
                "Ip": "0.0.0.0",
                "MemDesc": "8GB",
                "Spec": "CVM.S5",
                "StorageType": 5
            }
        ],
        "RequestId": "369660ea-8cdd-4079-b473-8eb14b059b53",
        "TotalCnt": 3
    }
}
```

