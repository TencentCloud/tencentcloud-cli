**Example 1: DescribeApiApp**



Input: 

```
tccli apigateway DescribeApiApp --cli-unfold-argument  \
    --ApiAppId app-kzofrjbl
```

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
                    "ApiAppKey": "",
                    "ApiAppSecret": "",
                    "CreatedTime": "2020-12-01T10:44:55Z",
                    "ModifiedTime": "2020-12-01T10:44:55Z",
                    "ApiAppDesc": ""
                }
            ]
        },
        "RequestId": "98f5e9a5-c31d-470c-a7a9-325dcbb41d5b"
    }
}
```

