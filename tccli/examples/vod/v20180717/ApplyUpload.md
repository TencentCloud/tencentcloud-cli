**Example 1: 申请上传成功例子**



Input: 

```
tccli vod ApplyUpload --cli-unfold-argument  \
    --SubAppId 1 \
    --MediaType mp4
```

Output: 
```
{
    "Response": {
        "CoverStoragePath": "/dir/cover.xx",
        "RequestId": "880f3005-a8c9-4bba-8c87-74e216a17a0b",
        "StorageBucket": "xadacq111211-100922",
        "StorageRegion": "ap-chongqing",
        "MediaStoragePath": "/dir/name.xx",
        "VodSessionKey": "VodSessionKey",
        "TempCertificate": {
            "SecretId": "xxxxxxx",
            "SecretKey": "xxxxxxxx",
            "Token": "xxxxxxxx",
            "ExpiredTime": 182823331
        }
    }
}
```

