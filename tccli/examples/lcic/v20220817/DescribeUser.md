**Example 1: 获取用户信息**



Input: 

```
tccli lcic DescribeUser --cli-unfold-argument  \
    --UserId abc
```

Output: 
```
{
    "Response": {
        "SdkAppId": 1,
        "UserId": "abc",
        "Name": "abc",
        "Avatar": "abc",
        "OriginId": "abc",
        "RequestId": "abc"
    }
}
```

