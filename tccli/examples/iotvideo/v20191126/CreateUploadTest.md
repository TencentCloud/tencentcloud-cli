**Example 1: 设备申请COS上传临时证书**



Input: 

```
tccli iotvideo CreateUploadTest --cli-unfold-argument  \
    --PkgId yc1m3d \
    --Tid ********
```

Output: 
```
{
    "Response": {
        "RequestId": "4f7cc74f-e442-431d-b447-50020076f725",
        "Data": {
            "StorageBucket": "9ba09148vodbj1259781373-10022853",
            "StorageRegion": "ap-beijing",
            "StoragePath": "/9ba09148vodbj1259781373/97addbdd5285890796668801187/",
            "SessionKey": "*******",
            "TempCertificate": {
                "SecretId": "*******",
                "SecretKey": "*******",
                "Token": "************",
                "ExpiredTime": 1577340790
            }
        }
    }
}
```

