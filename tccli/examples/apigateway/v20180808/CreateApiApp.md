**Example 1: CreateApiApp**



Input: 

```
tccli apigateway CreateApiApp --cli-unfold-argument  \
    --ApiAppName test
```

Output: 
```
{
    "Response": {
        "Result": {
            "ApiAppName": "testapp",
            "ApiAppId": "app-kzofrjbl",
            "ApiAppKey": "XXX",
            "ApiAppSecret": "XXX",
            "CreatedTime": "2020-12-01T10:44:55Z",
            "ModifiedTime": "2020-12-01T10:44:55Z",
            "ApiAppDesc": "first app"
        },
        "RequestId": "ad5218b4-edc3-4195-ba4d-a0ef176783ba"
    }
}
```

