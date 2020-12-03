**Example 1: 启用API**



Input: 

```
tccli tsf ChangeApiUsableStatus --cli-unfold-argument  \
    --ApiId api-d5970cd2 \
    --UsableStatus enabled
```

Output: 
```
{
    "Response": {
        "Result": {
            "UpdatedTime": "xx",
            "PathMapping": "xx",
            "MicroserviceName": "xx",
            "Description": "xx",
            "MicroserviceId": "xx",
            "NamespaceName": "xx",
            "ApiId": "api-d5970cd2",
            "UsableStatus": "xx",
            "ApiType": "xx",
            "ReleaseStatus": "xx",
            "GroupName": "xx",
            "Host": "xx",
            "Method": "POST",
            "RateLimitStatus": "xx",
            "Timeout": 10,
            "NamespaceId": "xx",
            "CreatedTime": "xx",
            "Path": "/provider-demo/v1/echo",
            "ReleasedTime": "xx",
            "MockStatus": "xx",
            "GroupId": "xx"
        },
        "RequestId": "5d996e5507e42d5970cd2e25ed5267a"
    }
}
```

