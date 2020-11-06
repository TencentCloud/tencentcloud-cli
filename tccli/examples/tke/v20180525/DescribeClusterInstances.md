**Example 1: 查询集群实例信息**

查询集群实例信息

Input: 

```
tccli tke DescribeClusterInstances --cli-unfold-argument  \
    --ClusterId cls-xxxxxx
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "InstanceSet": [
            {
                "InstanceId": "ins-gsk7l6vw",
                "InstanceRole": "WORKER",
                "InstanceState": "running",
                "FailedReason": ""
            }
        ],
        "RequestId": "82f2fe9c-c5fa-4077-9236-f1341180a696"
    }
}
```

