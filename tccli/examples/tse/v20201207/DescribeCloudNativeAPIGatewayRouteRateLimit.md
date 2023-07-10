**Example 1: 展示云原生网关限流插件(路由)**

展示云原生网关限流插件(路由)

Input: 

```
tccli tse DescribeCloudNativeAPIGatewayRouteRateLimit --cli-unfold-argument  \
    --GatewayId abc \
    --Id 6f423439-ec27-4a2e-aff9-9e73ffa3da4d
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
            "Path": "/gd",
            "Header": "abc",
            "LimitBy": "ip",
            "ExternalRedis": {
                "RedisHost": "abc",
                "RedisPassword": "abc",
                "RedisPort": 0,
                "RedisTimeout": 0
            },
            "Policy": "redis",
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
            "LineUpTime": 10,
            "IsDelay": true
        },
        "RequestId": "abc"
    }
}
```

