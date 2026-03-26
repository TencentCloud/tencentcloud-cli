**Example 1: 新增publish_key类型的key**



Input: 

```
tccli tcb CreateApiKey --cli-unfold-argument  \
    --EnvId env-123 \
    --KeyType publish_key
```

Output: 
```
{
    "Response": {
        "ApiKey": "eyJhbGciOiJSUzI1NiIsImtpZCskdfhss",
        "CreateAt": "2026-03-16T15:48:48+08:00",
        "ExpireAt": "2099-03-16T15:48:48+08:00",
        "KeyId": "6qBr24a4Tn3sKs1UZSsv_w",
        "Name": "publish_key",
        "RequestId": "fd103953-d395-449c-9f1d-ea3822e48af6"
    }
}
```

**Example 2: 新增90天过期的api_key类型的key**



Input: 

```
tccli tcb CreateApiKey --cli-unfold-argument  \
    --EnvId env-123 \
    --KeyType api_key \
    --KeyName server_key \
    --ExpireIn 7776000
```

Output: 
```
{
    "Response": {
        "ApiKey": "eyJhbGciOiJSUzI1NiIsImtpZCskdfhss",
        "CreateAt": "2026-03-16T15:48:48+08:00",
        "ExpireAt": "2026-06-16T15:48:48+08:00",
        "KeyId": "6qBr24a4Tn3sKs1UZSsv_w",
        "Name": "server_key",
        "RequestId": "ddea6362-324d-4485-b32c-7b93044639b1"
    }
}
```

