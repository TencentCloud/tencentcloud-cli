**Example 1: 请求示例**



Input: 

```
tccli eiam DecribePublicKey --cli-unfold-argument  \
    --ApplicationId xx
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "ApplicationId": "xx",
        "PublicKey": "{\"kty\":\"EC\",\"kid\":\"xxxxxxxxxxxxxxxxxx\",\"use\":\"sig\",\"alg\":\"ES256\",\"x\":\"xxxxxxxxxxxxxxxxxx\",\"y\":\"xxxxxxxxxxxxxxxxxx\",\"crv\":\"P-256\"}",
        "KeyId": "xx"
    }
}
```

