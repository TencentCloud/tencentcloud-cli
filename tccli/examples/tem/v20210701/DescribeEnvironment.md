**Example 1: 获取环境状态**

获取环境状态

Input: 

```
tccli tem DescribeEnvironment --cli-unfold-argument  \
    --EnvironmentId en-xxxxxx \
    --SourceChannel 0
```

Output: 
```
{
    "Response": {
        "Result": {
            "EnvironmentId": "en-xxxxxx",
            "NamespaceName": "abc",
            "Region": "ap-shanghai",
            "VpcId": "vpc-xxxxxx",
            "SubnetIds": [
                "subnet-xxxxxx"
            ],
            "Description": "abc",
            "CreatedDate": "abc",
            "EnvironmentName": "abc",
            "ApmInstanceId": "abc",
            "Locked": 0,
            "Tags": [
                {
                    "TagKey": "abc",
                    "TagValue": "abc"
                }
            ],
            "EnvType": "abc"
        },
        "RequestId": "abc-xxx-xxx"
    }
}
```

