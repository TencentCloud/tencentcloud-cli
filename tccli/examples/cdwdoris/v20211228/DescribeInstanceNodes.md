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
                "Ip": "abc",
                "Spec": "abc",
                "Core": 0,
                "Memory": 0,
                "DiskType": "abc",
                "DiskSize": 0,
                "Role": "abc",
                "Status": "abc",
                "Rip": "abc",
                "FeRole": "abc",
                "UUID": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

