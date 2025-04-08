**Example 1: 查询微信小程序信息**



Input: 

```
tccli lowcode DescribeWxAppInfo --cli-unfold-argument  \
    --ComponentAppId wx1g16kjpw7d155d7a \
    --WxAppId wx1g16kjpw7d155d7b
```

Output: 
```
{
    "Response": {
        "WxAppInfos": [
            {
                "ComponentAppId": "wx1g16kjpw7d155d7a",
                "WxAppId": "wx1g16kjpw7d155d7a",
                "AccessToken": "aa1g16kjpw7d155d7a",
                "NickName": "test",
                "ExpireTime": "2022-10-22 00:00:00"
            }
        ],
        "RequestId": "1g16kjpw7d155d7a"
    }
}
```

