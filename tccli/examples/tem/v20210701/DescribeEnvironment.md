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
        "RequestId": "85435f86-a454-4bf8-8e8c-074a51f55bb2",
        "Result": {
            "EnvironmentId": "en-l5mmxey5",
            "EnvironmentName": "bugfix-gz",
            "Region": "ap-guangzhou",
            "VpcId": "vpc-9xcgo41t",
            "SubnetIds": [
                "subnet-orcy48cy"
            ],
            "Description": "这是一个描述",
            "CreatedDate": "2024-07-01 17:48:35",
            "ApmInstanceId": "",
            "Locked": 0,
            "NamespaceName": "",
            "Tags": [],
            "EnvType": "prod"
        }
    }
}
```

