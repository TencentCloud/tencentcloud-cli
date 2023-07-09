**Example 1: 查询云原生网关限流插件(服务)**

查询云原生网关限流插件(服务)

Input: 

```
tccli tse DescribeCloudNativeAPIGatewayServiceRateLimit --cli-unfold-argument  \
    --GatewayId gateway-9abf3b79 \
    --Name test-service
```

Output: 
```
{
    "Response": {
        "Result": {
            "Enabled": true,
            "QpsThresholds": [
                {
                    "Unit": "second",
                    "Max": 10
                }
            ],
            "Path": "/ff",
            "Header": "abc",
            "LimitBy": "ip",
            "ExternalRedis": {
                "RedisHost": "abc",
                "RedisPassword": "abc",
                "RedisPort": 0,
                "RedisTimeout": 0
            },
            "Policy": "local",
            "RateLimitResponse": {
                "Body": "abc",
                "Headers": [
                    {
                        "Key": "abc",
                        "Value": "abc"
                    }
                ],
                "HttpStatus": 200
            },
            "RateLimitResponseUrl": "http://tencent.com/",
            "ResponseType": "url",
            "HideClientHeaders": true,
            "LineUpTime": 1,
            "IsDelay": true
        },
        "RequestId": "abc"
    }
}
```

