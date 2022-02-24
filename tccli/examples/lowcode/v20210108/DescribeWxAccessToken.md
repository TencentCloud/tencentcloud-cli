**Example 1: 生成token**



Input: 

```
tccli lowcode DescribeWxAccessToken --cli-unfold-argument  \
    --WxAppId xx \
    --ComponentAppId xx
```

Output: 
```
{
    "Response": {
        "Token": "xx",
        "RequestId": "xx",
        "ExpireAt": 1
    }
}
```

