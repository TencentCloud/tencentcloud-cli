**Example 1: 获取当前集群各用户绑定的资源信息**



Input: 

```
tccli cdwdoris DescribeUserBindWorkloadGroup --cli-unfold-argument  \
    --InstanceId cdwdoris-xxx
```

Output: 
```
{
    "Response": {
        "RequestId": "ddbf7259-7486-4980-a8dc-88c557866f0a",
        "UserBindInfos": [
            {
                "UserName": "user1",
                "WorkloadGroupName": "g1"
            },
            {
                "UserName": "admin",
                "WorkloadGroupName": "normal"
            }
        ]
    }
}
```

