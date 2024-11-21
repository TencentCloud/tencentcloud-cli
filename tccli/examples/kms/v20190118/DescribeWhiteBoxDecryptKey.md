**Example 1: 获取白盒解密密钥**



Input: 

```
tccli kms DescribeWhiteBoxDecryptKey --cli-unfold-argument  \
    --KeyId 244dab8c-6dad-11ea-80c6-5254006d0810
```

Output: 
```
{
    "Response": {
        "RequestId": "8788b5f3-8eaa-48a8-915a-b7c52f57065e",
        "DecryptKey": "AAAAACL4R9T1M3r3/S9XpMbUbwHJUKbq/tll0Bop7LG90lHpj+DKmOiEE0Rs5rRrMN*****qaf0ot57NzfuWG92oAe9HQ7bDCcfuBN7nXX+QipQIBxD/LVWk7zrHtLD/TJfAAoTuE7QKc/lSTOpI1xkTxJq/AFLd5K9EaBN7kpAkAsponZc20Tpk+KlyWE3NHdQrION9fsxtUBl5tz/l6T1j49SR5J2axZ2nnkA3o7L1WIGiv7r3tkd+"
    }
}
```

