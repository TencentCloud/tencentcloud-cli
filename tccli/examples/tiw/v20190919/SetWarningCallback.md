**Example 1: 设置告警回调地址**

设置告警回调地址

Input: 

```
tccli tiw SetWarningCallback --cli-unfold-argument  \
    --SdkAppId 123456 \
    --Callback http://callback \
    --CallbackKey 123456
```

Output: 
```
{
    "Response": {
        "RequestId": "786eafde-17a8-47a9-9e1c-05b2b282dccc"
    }
}
```

