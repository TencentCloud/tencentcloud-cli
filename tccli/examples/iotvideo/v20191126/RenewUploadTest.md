**Example 1: 设备刷新临时证书**



Input: 

```
tccli iotvideo RenewUploadTest --cli-unfold-argument  \
    --PkgId yc1m3d \
    --Tid ******** \
    --SessionKey ***********
```

Output: 
```
{
    "Response": {
        "RequestId": "0ff2ba1b-0423-438d-8505-d34774072bfe",
        "Data": {
            "TempCertificate": {
                "SecretId": "***********",
                "SecretKey": "***********",
                "Token": "**********",
                "ExpiredTime": 1577340489
            }
        }
    }
}
```

