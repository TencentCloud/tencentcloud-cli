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
            "Region": "ap-shanghai",
            "VpcId": "vpc-xxx",
            "SubnetIds": [
                "subnet-xxx"
            ],
            "Description": "vpc-xxx",
            "CreatedDate": "2011-11-11"
        },
        "RequestId": "xx"
    }
}
```

