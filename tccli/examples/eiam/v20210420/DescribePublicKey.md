**Example 1: 请求示例**



Input: 

```
tccli eiam DescribePublicKey --cli-unfold-argument  \
    --ApplicationId xxx
```

Output: 
```
{
    "Response": {
        "RequestId": "xxx",
        "ApplicationId": "xxx",
        "PublicKey": "{\"kty\":\"EC\",\"kid\":\"xxx\",\"use\":\"sig\",\"alg\":\"ES256\",\"x\":\"xxx\",\"y\":\"xxx\",\"crv\":\"P-256\"}",
        "KeyId": "xxx"
    }
}
```

