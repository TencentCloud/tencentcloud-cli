**Example 1: 拉取APM实例列表**

拉取APM实例列表

Input: 

```
tccli apm DescribeApmInstances --cli-unfold-argument  \
    --Tags.0.Key appid \
    --Tags.0.Value 1231
```

Output: 
```
{
    "Response": {
        "Instances": [
            {
                "Name": "测试使用",
                "InstanceId": "3bxumb01ul",
                "Description": "测试使用",
                "AppId": 251005942,
                "CreateUin": 1618331756
            }
        ],
        "RequestId": "xxvi8hvszwk2b293tvjzjpezi5hx-gvm"
    }
}
```

