**Example 1: 请求示例**



Input: 

```
tccli eiam DescribeApplication --cli-unfold-argument  \
    --ApplicationId xxx
```

Output: 
```
{
    "Response": {
        "RequestId": "efe4663a-f71b-498d-a270-0cca0c69f743",
        "ApplicationId": "52edd4a7-cd07-4ab1-8f33-8bb537179ba2",
        "DisplayName": "测试API网关应用",
        "CreatedDate": "2020-05-28T02:09:57.343+00:00",
        "LastModifiedDate": "2020-11-26T03:41:21.891+00:00",
        "ApplicationType": "API",
        "TokenExpired": "4800",
        "ClientId": "xxx",
        "ClientSecret": "xxx",
        "KeyId": "xxx",
        "PublicKey": "{\"kty\":\"RSA\",\"kid\":\"xxx\",\"use\":\"sig\",\"alg\":\"RS256\",\"n\":\"xxx\",\"e\":\"AQAB\"}",
        "AuthorizeUrl": "https://xxx.com/auth/oauth2/authorize?client_id=xxx&response_type=code&state=xxx",
        "IconUrl": "https://online-xxxxxxx.cos.ap-shenzhen-fsi.myqcloud.com/xxxxxxxx/...",
        "SecureLevel": "1",
        "AppStatus": true,
        "Description": "xxxxxxxxxxxxx"
    }
}
```

