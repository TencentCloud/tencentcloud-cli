**Example 1: 获取环境状态**

获取环境状态

Input: 

```
tccli tem DescribeEnvironment --cli-unfold-argument  \
    --EnvironmentId xx \
    --SourceChannel 0
```

Output: 
```
{
    "Response": {
        "Result": {
            "EnvironmentId": "xx",
            "VpcId": "xx",
            "Locked": 0,
            "Description": "xx",
            "EnvironmentName": "xx",
            "NamespaceName": "xx",
            "Region": "xx",
            "Tags": [
                {
                    "TagKey": "xx",
                    "TagValue": "xx"
                }
            ],
            "ApmInstanceId": "xx",
            "CreatedDate": "xx",
            "SubnetIds": [
                "subnet-xxx"
            ]
        },
        "RequestId": "xx"
    }
}
```

