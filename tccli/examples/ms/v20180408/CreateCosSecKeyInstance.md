**Example 1: 获取COS临时密钥**



Input: 

```
tccli ms CreateCosSecKeyInstance --cli-unfold-argument  \
    --CosRegion ap-guangzhou
```

Output: 
```
{
    "Response": {
        "CosAppid": 123456,
        "CosBucket": "ms-shield",
        "CosId": "XXXXzgG3O5Cm9ii31sTgph1XhFISnvKPw0Zi",
        "CosKey": "55VuqLWV4HKvuYom4tYkn6FdXpVoM7hz",
        "CosPrefix": "pctool/123456789/1542613158",
        "CosRegion": "ap-guangzhou",
        "CosTocken": "13606435fd46b2765dd01aa4eaf356dfca88817030001",
        "ExpireTime": 3600,
        "RequestId": "ce5e66e0-aab5-4d31-9b98-c52caf0fdfae"
    }
}
```

