**Example 1: 查询路径重写列表**



Input: 

```
tccli tsf DescribePathRewrites --cli-unfold-argument  \
    --GatewayGroupId group-yd3b588a \
    --SearchWord app \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "a9010490-6c80-4e53-8953-5493d8899460",
        "Result": {
            "Content": [
                {
                    "Blocked": "N",
                    "GatewayGroupId": "group-yd3b588a",
                    "Order": 1,
                    "PathRewriteId": "rewrite-2vz5pdwv",
                    "Regex": "/app",
                    "Replacement": "/user"
                }
            ],
            "TotalCount": 1
        }
    }
}
```

