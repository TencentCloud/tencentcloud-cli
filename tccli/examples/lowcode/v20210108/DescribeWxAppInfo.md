**Example 1: 查询微信小程序信息**



Input: 

```
tccli lowcode DescribeWxAppInfo --cli-unfold-argument  \
    --ComponentAppId abc \
    --WxAppId abc
```

Output: 
```
{
    "Response": {
        "WxAppInfos": [
            {
                "ComponentAppId": "abc",
                "WxAppId": "abc",
                "AccessToken": "abc",
                "NickName": "abc",
                "ExpireTime": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

