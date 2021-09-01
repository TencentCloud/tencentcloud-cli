**Example 1: 设置登录保护校验方式为微信**



Input: 

```
tccli cam SetMfaFlag --cli-unfold-argument  \
    --LoginFlag.Phone 1 \
    --LoginFlag.Stoken 1 \
    --LoginFlag.Wechat 1 \
    --OpUin 1 \
    --ActionFlag.Phone 1 \
    --ActionFlag.Stoken 1 \
    --ActionFlag.Wechat 1
```

Output: 
```
{
    "Response": {
        "RequestId": "cf75531d-b72d-4dcb-b0ed-d1c029a37f38"
    }
}
```

