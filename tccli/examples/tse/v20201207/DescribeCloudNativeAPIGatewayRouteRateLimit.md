**Example 1: 展示云原生网关限流插件(路由)**

展示云原生网关限流插件(路由)

Input: 

```
tccli tse DescribeCloudNativeAPIGatewayRouteRateLimit --cli-unfold-argument  \
    --GatewayId gateway-dde03767 \
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
            "Path": "/v1/users",
            "Header": "app",
            "LimitBy": "ip",
            "ExternalRedis": {
                "RedisHost": "172.168.20.20",
                "RedisPassword": "avkj32671@",
                "RedisPort": 6379,
                "RedisTimeout": 3
            },
            "Policy": "redis",
            "RateLimitResponse": {
                "Body": "Too Many Requests",
                "Headers": [
                    {
                        "Key": "ratelimit",
                        "Value": "ratelimit"
                    }
                ],
                "HttpStatus": 429
            },
            "RateLimitResponseUrl": "http://tencent.com/",
            "ResponseType": "url",
            "HideClientHeaders": true,
            "LineUpTime": 10,
            "IsDelay": true
        },
        "RequestId": "ffadafb6-545d-461c-ad8c-baa26c0f8955"
    }
}
```

