**Example 1: 查询路径重写**



Input: 

```
tccli tsf DescribePathRewrite --cli-unfold-argument  \
    --PathRewriteId rewrite-2vz5pdwv
```

Output: 
```
{
    "Response": {
        "RequestId": "bc1c265c-bce0-4d9b-82bc-592668daf7af",
        "Result": {
            "Blocked": "N",
            "GatewayGroupId": "group-yd3b588a",
            "Order": 1,
            "PathRewriteId": "rewrite-2vz5pdwv",
            "Regex": "/app",
            "Replacement": "/user"
        }
    }
}
```

