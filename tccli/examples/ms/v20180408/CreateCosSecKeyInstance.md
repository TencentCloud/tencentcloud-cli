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
        "CosBucket": "ms-shield",
        "CosRegion": "ap-guangzhou",
        "ExpireTime": 1,
        "CosId": "XXXXzgG3O5Cm9ii31sTgph1XhFISnvKPw0Zi",
        "CosKey": "XXXXV4HKvuYom4tYkn6FdXpVoM7hz",
        "CosPrefix": "pctool/123456789/1542613158",
        "CosToken": "13606435fd46b2765dd01aa4eaf356dfxxxxxx",
        "RequestId": "RequestId-xxxxxxx"
    }
}
```

