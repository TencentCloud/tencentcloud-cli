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
        "RequestId": "3b3f064b-1d0f-4b36-8c04-f0d98b77fa98",
        "ApplicationId": "606bacf8-544a-4907-bbd7-d925c86f58ca",
        "PublicKey": "{\"kty\":\"EC\",\"kid\":\"90A7CB2BFA574F62AC4A3FC343279619\",\"use\":\"sig\",\"alg\":\"ES256\",\"x\":\"gXaBcr7DwfN-uzrMQbDBs6Nzh7G5yzsArvXCALOssjA\",\"y\":\"MmPQ84lxEP_gGqMEC-6qoikcYmkbm3frKbbwkxI-E3g\",\"crv\":\"P-256\"}",
        "KeyId": "90A7CB2BFA574F62AC4A3FC343279619"
    }
}
```

