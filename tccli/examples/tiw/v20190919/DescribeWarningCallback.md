**Example 1: 获取告警回调地址信息**

获取告警回调地址信息

Input: 

```
tccli tiw DescribeWarningCallback --cli-unfold-argument  \
    --SdkAppId 123456
```

Output: 
```
{
    "Response": {
        "Callback": "http://callback",
        "CallbackKey": "12345",
        "RequestId": "786eafde-17a8-47a9-9e1c-05b2b282dccc"
    }
}
```

