**Example 1: 查询已经存在的节点**

查询已经存在的节点，判断是否可以加入集群

Input: 

```
tccli tke DescribeExistedInstances --cli-unfold-argument  \
    --ClusterId cls-xxxxxxxx
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "ExistedInstanceSet": [
            {
                "Usable": true,
                "UnusableReason": "",
                "AlreadyInCluster": "",
                "InstanceId": "ins-xxxxxxxx",
                "InstanceName": "未命名",
                "PrivateIpAddresses": [
                    "192.168.x.x"
                ],
                "PublicIpAddresses": [
                    "118.24.x.x"
                ],
                "CreatedTime": "2019-05-13T03:37:24Z",
                "CPU": 2,
                "Memory": 4,
                "OsName": "Ubuntu xxxxxxxxx",
                "InstanceType": "Sxxxxxx"
            }
        ],
        "RequestId": "f12a6e20-f950-4af9-8f8b-b6329a4961c2"
    }
}
```

