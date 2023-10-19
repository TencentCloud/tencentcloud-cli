**Example 1: 获取专享实例用户信息**

获取专享实例用户信息

Input: 

```
tccli apigateway DescribeUserInfoByInstanceIP --cli-unfold-argument  \
    --IP 119.0.0.1
```

Output: 
```
{
    "Response": {
        "RequestId": "44f6a1fc-c29e-4109-8a52-3f5b5ecd72e8",
        "Result": {
            "AppId": 12000000,
            "BaradAppId": 13000000,
            "InstanceId": "instance-xxxxx",
            "InstanceName": "test",
            "Uin": "1000000009"
        }
    }
}
```

