**Example 1: DescribeApiEnvironmentStrategy**

用于展示API绑定的限流策略。

Input: 

```
tccli apigateway DescribeApiEnvironmentStrategy --cli-unfold-argument  \
    --ServiceId service-ody35h5e \
    --EnvironmentNames test
```

Output: 
```
{
    "Response": {
        "Result": {
            "TotalCount": 12,
            "ApiEnvironmentStrategySet": [
                {
                    "ApiId": "api-ne9wyb30",
                    "ApiName": "hadongtestapi_ed3f0c",
                    "Path": "/pathtest03",
                    "Method": "GET",
                    "EnvironmentStrategySet": [
                        {
                            "EnvironmentName": "test",
                            "Quota": -1
                        }
                    ]
                },
                {
                    "ApiId": "api-k3ezsaoi",
                    "ApiName": "name",
                    "Path": "/lkjdszfhbgv",
                    "Method": "GET",
                    "EnvironmentStrategySet": [
                        {
                            "EnvironmentName": "test",
                            "Quota": -1
                        }
                    ]
                },
                {
                    "ApiId": "api-04h0i7z0",
                    "ApiName": "name",
                    "Path": "/lkjhbgv",
                    "Method": "GET",
                    "EnvironmentStrategySet": [
                        {
                            "EnvironmentName": "test",
                            "Quota": -1
                        }
                    ]
                },
                {
                    "ApiId": "api-qsmlelcu",
                    "ApiName": "name",
                    "Path": "/cfgvbhjgfdn",
                    "Method": "GET",
                    "EnvironmentStrategySet": [
                        {
                            "EnvironmentName": "test",
                            "Quota": -1
                        }
                    ]
                },
                {
                    "ApiId": "api-g0wgjcz8",
                    "ApiName": "name",
                    "Path": "/ghkjhbhvb",
                    "Method": "GET",
                    "EnvironmentStrategySet": [
                        {
                            "EnvironmentName": "test",
                            "Quota": -1
                        }
                    ]
                },
                {
                    "ApiId": "api-c6d2x8fk",
                    "ApiName": "name",
                    "Path": "/testxxx",
                    "Method": "GET",
                    "EnvironmentStrategySet": [
                        {
                            "EnvironmentName": "test",
                            "Quota": -1
                        }
                    ]
                },
                {
                    "ApiId": "api-gsd5bks6",
                    "ApiName": "name",
                    "Path": "/tsf",
                    "Method": "GET",
                    "EnvironmentStrategySet": [
                        {
                            "EnvironmentName": "test",
                            "Quota": -1
                        }
                    ]
                },
                {
                    "ApiId": "api-jmh3naag",
                    "ApiName": "name",
                    "Path": "/mytest",
                    "Method": "GET",
                    "EnvironmentStrategySet": [
                        {
                            "EnvironmentName": "test",
                            "Quota": -1
                        }
                    ]
                },
                {
                    "ApiId": "api-7kcivknq",
                    "ApiName": "name",
                    "Path": "/bsdbsddd",
                    "Method": "GET",
                    "EnvironmentStrategySet": [
                        {
                            "EnvironmentName": "test",
                            "Quota": -1
                        }
                    ]
                },
                {
                    "ApiId": "api-4beu85p0",
                    "ApiName": "name",
                    "Path": "/xxxxxx",
                    "Method": "GET",
                    "EnvironmentStrategySet": [
                        {
                            "EnvironmentName": "test",
                            "Quota": -1
                        }
                    ]
                },
                {
                    "ApiId": "api-qctp0evy",
                    "ApiName": "name",
                    "Path": "/",
                    "Method": "GET",
                    "EnvironmentStrategySet": []
                },
                {
                    "ApiId": "api-e92i2jds",
                    "ApiName": "test2",
                    "Path": "/users",
                    "Method": "POST",
                    "EnvironmentStrategySet": [
                        {
                            "EnvironmentName": "test",
                            "Quota": -1
                        }
                    ]
                },
                {
                    "ApiId": "api-3v4tzy3u",
                    "ApiName": "test1",
                    "Path": "/users/{name}",
                    "Method": "GET",
                    "EnvironmentStrategySet": [
                        {
                            "EnvironmentName": "test",
                            "Quota": -1
                        }
                    ]
                }
            ]
        },
        "RequestId": "6b191d6c-dbdd-4214-b464-b7385ff01e15"
    }
}
```

