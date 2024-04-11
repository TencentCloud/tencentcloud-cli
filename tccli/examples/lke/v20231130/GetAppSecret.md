**Example 1: 获取应用密钥**



Input: 

```
tccli lke GetAppSecret --cli-unfold-argument  \
    --LoginUin abc \
    --LoginSubAccountUin abc \
    --AppBizId abc
```

Output: 
```
{
    "Response": {
        "AppKey": "",
        "CreateTime": "",
        "IsRelease": false,
        "HasPermission": true,
        "RequestId": "abc"
    }
}
```

