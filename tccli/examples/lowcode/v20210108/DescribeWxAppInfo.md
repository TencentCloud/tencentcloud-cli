**Example 1: 查询微信小程序信息**



Input: 

```
tccli lowcode DescribeWxAppInfo --cli-unfold-argument  \
    --ComponentAppId xx
```

Output: 
```
{
    "Response": {
        "WxAppInfos": [
            {
                "ExpireTime": "xx",
                "WxAppId": "xx",
                "ComponentAppId": "xx",
                "NickName": "xx",
                "AccessToken": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

