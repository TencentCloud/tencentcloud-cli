**Example 1: GetCosToken 示例**

开发空间-获取cos token

Input: 

```
tccli wedata GetCosToken --cli-unfold-argument  \
    --ProjectId abc \
    --OriginDomain abc \
    --BucketName abc \
    --RemotePath abc \
    --CrossFlag True
```

Output: 
```
{
    "Response": {
        "Region": "abc",
        "Token": {
            "Id": "abc",
            "Token": "abc",
            "SecretId": "abc",
            "SecretKey": "abc",
            "Response": "abc",
            "OwnerUin": "abc",
            "ExpiredTime": 1,
            "CreateTime": 1,
            "UpdateTime": 1,
            "OperatorUin": "abc"
        },
        "Bucket": "abc",
        "EndPoint": "abc",
        "RequestId": "abc"
    }
}
```

