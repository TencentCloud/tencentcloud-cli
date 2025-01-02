**Example 1: 获取集群节点信息列表**

获取集群节点信息列表

Input: 

```
tccli cdwdoris DescribeInstanceNodes --cli-unfold-argument  \
    --InstanceId cdwch-12345678
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "InstanceNodesList": [
            {
                "Ip": "9.0.16.4",
                "Spec": "S_4_16_H",
                "Core": 0,
                "Memory": 0,
                "DiskType": "CLOUD_SSD",
                "DiskSize": 0,
                "Role": "core",
                "Status": "Running",
                "Rip": "9.0.16.8",
                "FeRole": "core",
                "UUID": "a890x"
            }
        ],
        "RequestId": "abc-xa2"
    }
}
```

