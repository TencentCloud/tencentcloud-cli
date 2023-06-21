**Example 1: 申请扮演角色临时访问凭证**

申请扮演角色临时访问凭证

Input: 

```
tccli sts AssumeRole --cli-unfold-argument  \
    --RoleArn qcs%3A%3Acam%3A%3Auin%2F2385420691%3Arole%2F4611686018427397919 \
    --RoleSessionName cts
```

Output: 
```
{
    "Response": {
        "Credentials": {
            "Token": "da1e9d2ee9d***2dfe340001",
            "TmpSecretId": "AKID65zyIP0mpXtaI******WIQVMn1umNH58",
            "TmpSecretKey": "q95K84wrzuEGoc*******52boxvp71yoh"
        },
        "ExpiredTime": 1543914376,
        "Expiration": "2018-12-04T09:06:16Z",
        "RequestId": "4daec797-9cd2-4f09-9e7a-7d4c43b2a74c"
    }
}
```

