**Example 1: 查询路径重写列表**



Input: 

```
tccli tsf DescribePathRewrites --cli-unfold-argument  \
    --GatewayGroupId group-12345
```

Output: 
```
{
    "Response": {
        "Result": {
            "Content": [
                {
                    "Regex": "^(.*)$",
                    "PathRewriteId": "xx",
                    "GatewayGroupId": "xx",
                    "Replacement": "/s/ns/ms/$1",
                    "Order": 0,
                    "Blocked": "xx"
                }
            ],
            "TotalCount": 1
        },
        "RequestId": "xx"
    }
}
```

