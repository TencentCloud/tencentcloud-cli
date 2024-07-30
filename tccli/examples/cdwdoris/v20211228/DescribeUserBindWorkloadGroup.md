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
        "RequestId": "abc",
        "UserBindInfos": [
            {
                "UserName": "test",
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

