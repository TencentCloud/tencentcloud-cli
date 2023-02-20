**Example 1: 获取全程票据**



Input: 

```
tccli sts GetServiceTokenForInternal --cli-unfold-argument  \
    --TargetUin 100000000001 \
    --TargetOwnerUin 10000000001 \
    --TargetAction DescribeInstances
```

Output: 
```
{
    "Response": {
        "Credentials": {
            "Token": "da1e9d2ee9dda83506832d5ecb903b790132dfe340001",
            "TmpSecretId": "AKID65zyIP0mpXtaI******WIQVMn1umNH58",
            "TmpSecretKey": "q95K84wrzuEGoc*******52boxvp71yoh"
        },
        "ExpiredTime": 1543914376,
        "Expiration": "2018-12-04T09:06:16Z",
        "RequestId": "4daec797-9cd2-4f09-9e7a-7d4c43b2a74c"
    }
}
```

