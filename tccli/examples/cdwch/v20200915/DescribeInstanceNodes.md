**Example 1: 获取实例节点信息列表**

获取实例节点信息列表

Input: 

```
tccli cdwch DescribeInstanceNodes --cli-unfold-argument  \
    --InstanceId cdwch-12345678
```

Output: 
```
{
    "Response": {
        "RequestId": "f510b0e8-4bc7-44c7-a191-79e467b556c4",
        "TotalCount": 2,
        "InstanceNodesList": [
            {
                "Ip": "172.31.1.5",
                "Spec": "CVM.SA2",
                "Core": 16,
                "Memory": 32,
                "DiskType": "CLOUD_PREMIUM",
                "DiskSize": 1000,
                "Cluster": "default-cluster"
            },
            {
                "Ip": "172.31.1.4",
                "Spec": "CVM.SA2",
                "Core": 16,
                "Memory": 32,
                "DiskType": "CLOUD_PREMIUM",
                "DiskSize": 1000,
                "Cluster": "default-cluster"
            }
        ]
    }
}
```

