**Example 1: DescribeApiAppBindApisStatus**



Input: 

```
tccli apigateway DescribeApiAppBindApisStatus --cli-unfold-argument  \
    --ApiAppId app-kzofrjbl
```

Output: 
```
{
    "Response": {
        "Result": {
            "TotalCount": 1,
            "ApiAppApiSet": [
                {
                    "ApiAppId": "app-kzofrjbl",
                    "ApiAppName": "testapp",
                    "ApiId": "api-c6piso8y",
                    "ApiName": "dsadasd",
                    "ServiceId": "service-j0fmd8x0",
                    "ApiRegion": "chongqing",
                    "EnvironmentName": "release",
                    "AuthorizedTime": "2020-12-03 14:58:04"
                }
            ]
        },
        "RequestId": "98f5e9a5-c31d-470c-a7a9-325dcbb41d5b"
    }
}
```

