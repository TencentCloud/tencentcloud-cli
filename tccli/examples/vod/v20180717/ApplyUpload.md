**Example 1: Successfully applying for upload**



Input: 

```
tccli vod ApplyUpload --cli-unfold-argument  \
    --MediaType mp4 \
    --SubAppId 1
```

Output: 
```
{
    "Response": {
        "CoverStoragePath": null,
        "RequestId": "880f3005-a8c9-4bba-8c87-74e216a17a0b",
        "StorageBucket": "xadagzp111211-100922",
        "StorageRegion": "ap-guangzhou-2",
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

