**Example 1: 生成token**



Input: 

```
tccli lowcode DescribeWxAccessToken --cli-unfold-argument  \
    --WxAppId abc \
    --ComponentAppId abc
```

Output: 
```
{
    "Response": {
        "Token": "abc",
        "ExpireAt": 1,
        "RequestId": "abc"
    }
}
```

