**Example 1: DescribeApiAppsStatus**



Input: 

```
tccli apigateway DescribeApiAppsStatus --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Result": {
            "TotalCount": 1,
            "ApiAppSet": [
                {
                    "ApiAppName": "testapp",
                    "ApiAppId": "app-kzofrjbl",
                    "ApiAppKey": "xxx",
                    "ApiAppSecret": "xxx",
                    "CreatedTime": "2020-12-01T10:44:55Z",
                    "ModifiedTime": "2020-12-01T10:44:55Z",
                    "ApiAppDesc": "first app"
                }
            ]
        },
        "RequestId": "98f5e9a5-c31d-470c-a7a9-325dcbb41d5b"
    }
}
```

