**Example 1: 创建COS临时凭证**



Input: 

```
tccli wedata CreateCosTempCredential --cli-unfold-argument  \
    --WorkspaceId 1 \
    --StorageType DLC \
    --Operation upload \
    --FilePath None \
    --Prefix None
```

Output: 
```
{
    "Response": {
        "Data": {
            "Bucket": "dlce45c-700002164618-1762244884-700001779129-251301051",
            "Expiration": "",
            "ExpiredTime": "1764751738",
            "PathPrefix": "/1300055887/.system/import/20251203/8ffda7f0-ce5d-4595-8019-f2610ba8e2ea/",
            "Region": "ap-guangzhou",
            "SessionToken": "2kyHbxn14ztoJlLO*****cVl7qwy7N",
            "StartTime": "1764749938",
            "TempSecretId": "AKIDmJfdfkVZ******QZYolT",
            "TempSecretKey": "s2M3Z1Z******qcp3f0=",
            "UploadUrl": "https://dlce45c-700002164618-1762244884-700001779129-251301051.cos.ap-guangzhou.myqcloud.com"
        },
        "RequestId": "acfb1919-614d-4423-9f81-64f8941dd52e"
    }
}
```

