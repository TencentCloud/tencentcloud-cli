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
        "TotalCnt": 3,
        "NodeList": [
            {
                "ExpireTime": "xx",
                "EmrResourceId": "xx",
                "MemDesc": "xx",
                "StorageType": 5,
                "Ip": "xx",
                "CpuNum": 8,
                "Flag": 1,
                "DiskSize": "xx",
                "Spec": "xx"
            },
            {
                "CpuNum": 8,
                "EmrResourceId": "xx",
                "MemDesc": "xx",
                "StorageType": 5,
                "Ip": "xx",
                "ExpireTime": "xx",
                "Flag": 2,
                "DiskSize": "xx",
                "Spec": "xx"
            },
            {
                "CpuNum": 8,
                "EmrResourceId": "xx",
                "MemDesc": "xx",
                "StorageType": 5,
                "Ip": "xx",
                "ExpireTime": "xx",
                "Flag": 2,
                "DiskSize": "xx",
                "Spec": "xx"
            }
        ],
        "RequestId": "xx",
        "MetaInfo": [
            "xx"
        ]
    }
}
```

