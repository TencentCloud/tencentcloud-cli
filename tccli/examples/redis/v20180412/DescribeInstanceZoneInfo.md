**Example 1: 请求示例**

查询指定实例的节点信息

Input: 

```
tccli redis DescribeInstanceZoneInfo --cli-unfold-argument  \
    --InstanceId crs-6tl7****
```

Output: 
```
{
    "Response": {
        "ReplicaGroups": [
            {
                "GroupId": 125101,
                "GroupName": "",
                "ZoneId": "ap-guangzhou-2",
                "Role": "master",
                "RedisNodes": [
                    {
                        "Keys": 39,
                        "Slot": "0-16383",
                        "Status": "normal",
                        "Role": "master",
                        "NodeId": "5f83a663d58f092f4791630065cb3a76c50b40a5"
                    }
                ]
            },
            {
                "GroupId": 125102,
                "GroupName": "ng-1",
                "ZoneId": "ap-guangzhou-3",
                "Role": "replica",
                "RedisNodes": [
                    {
                        "Keys": 0,
                        "Slot": "",
                        "Status": "normal",
                        "Role": "replica",
                        "NodeId": "bdc6d645f4741948cf51f93f7013edd64f44c3ba"
                    }
                ]
            }
        ],
        "RequestId": "e3d683fc-f2ff-43c9-980d-fae7a1166abc",
        "TotalCount": 2
    }
}
```

