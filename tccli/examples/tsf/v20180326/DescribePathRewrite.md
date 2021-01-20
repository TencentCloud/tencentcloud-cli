**Example 1: 查询路径重写**



Input: 

```
tccli tsf DescribePathRewrite --cli-unfold-argument  \
    --PathRewriteId rewrite-l6ymbvgd
```

Output: 
```
{
    "Response": {
        "Result": {
            "Regex": "^(.*)^",
            "PathRewriteId": "rewrite-l6ymbvgd",
            "GatewayGroupId": "group-123",
            "Replacement": "/s/ns/ms/$1",
            "Order": 0,
            "Blocked": "xx"
        },
        "RequestId": "xx"
    }
}
```

