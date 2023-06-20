**Example 1: 获取COS临时密钥**

获取COS临时密钥

Input: 

```
tccli ms CreateCosSecKeyInstance --cli-unfold-argument  \
    --CosRegion ap-guangzhou
```

Output: 
```
{
    "Response": {
        "CosAppid": 1,
        "CosBucket": "abc",
        "CosRegion": "abc",
        "ExpireTime": 1,
        "CosId": "abc",
        "CosKey": "abc",
        "CosTocken": "abc",
        "CosPrefix": "abc",
        "CosToken": "abc",
        "RequestId": "abc"
    }
}
```

