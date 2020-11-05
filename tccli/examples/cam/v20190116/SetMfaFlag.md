**Example 1: Setting login account verification to WeChat**



Input: 

```
tccli cam SetMfaFlag --cli-unfold-argument  \
    --OpUin 1234567\
    --LoginFlag.Wechat 1
```

Output: 
```
{
    "Response": {
        "RequestId": "cf75531d-b72d-4dcb-b0ed-d1c029a37f38"
    }
}
```

