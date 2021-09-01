**Example 1: DescribeAllPluginApis**



Input: 

```
tccli apigateway DescribeAllPluginApis --cli-unfold-argument  \
    --PluginId Plugin-23sdcda \
    --EnvironmentName release \
    --ServiceId service-jzo37opy
```

Output: 
```
{
    "Response": {
        "Result": {
            "TotalCount": 2,
            "ApiSet": [
                {
                    "ApiId": "api-hjqpe4dg",
                    "ApiName": "notbind",
                    "ApiType": "NORMAL",
                    "Path": "/notbind",
                    "Method": "GET",
                    "IsAttached": false,
                    "AttachedOtherPlugin": false
                },
                {
                    "ApiId": "api-1clczx66",
                    "ApiName": "mock2",
                    "ApiType": "NORMAL",
                    "Path": "/mock2",
                    "Method": "GET",
                    "IsAttached": false,
                    "AttachedOtherPlugin": true
                }
            ]
        },
        "RequestId": "5aaeb03a-8f00-4644-95e8-6307b1690aa2"
    }
}
```

