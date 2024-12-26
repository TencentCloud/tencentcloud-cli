**Example 1: 请求示例**



Input: 

```
tccli live DescribeLiveRecordTemplates --cli-unfold-argument  \
    --IsDelayLive 1
```

Output: 
```
{
    "Response": {
        "RequestId": "bc76b15f-734f-4bb5-9b0d-b3a1ecd5444d",
        "Templates": [
            {
                "AacParam": {
                    "ClassId": 0,
                    "CosBucketName": "",
                    "CosBucketPath": "",
                    "CosBucketRegion": "",
                    "Enable": 0,
                    "Procedure": "",
                    "RecordInterval": 1800,
                    "StorageMode": "normal",
                    "StorageTime": 0,
                    "VodFileName": "",
                    "VodSubAppId": 251006352
                },
                "CosStore": 0,
                "Description": "",
                "FlvParam": {
                    "ClassId": null,
                    "CosBucketName": "",
                    "CosBucketPath": "",
                    "CosBucketRegion": "",
                    "Enable": 1,
                    "Procedure": "",
                    "RecordInterval": 1800,
                    "StorageMode": "normal",
                    "StorageTime": 4572,
                    "VodFileName": "",
                    "VodSubAppId": 251006352
                },
                "FlvSpecialParam": {
                    "UploadInRecording": true
                },
                "HlsParam": {
                    "ClassId": 0,
                    "CosBucketName": "",
                    "CosBucketPath": "",
                    "CosBucketRegion": "",
                    "Enable": 0,
                    "Procedure": "",
                    "RecordInterval": 1800,
                    "StorageMode": "normal",
                    "StorageTime": 0,
                    "VodFileName": "",
                    "VodSubAppId": 251006352
                },
                "HlsSpecialParam": {
                    "FlowContinueDuration": 0
                },
                "IsDelayLive": 0,
                "Mp3Param": {
                    "ClassId": null,
                    "CosBucketName": "",
                    "CosBucketPath": "",
                    "CosBucketRegion": "",
                    "Enable": 0,
                    "Procedure": "",
                    "RecordInterval": 1800,
                    "StorageMode": "normal",
                    "StorageTime": 0,
                    "VodFileName": "",
                    "VodSubAppId": 251006352
                },
                "Mp4Param": {
                    "ClassId": 0,
                    "CosBucketName": "",
                    "CosBucketPath": "",
                    "CosBucketRegion": "",
                    "Enable": 0,
                    "Procedure": "",
                    "RecordInterval": 1800,
                    "StorageMode": "normal",
                    "StorageTime": 0,
                    "VodFileName": "",
                    "VodSubAppId": 251006352
                },
                "RemoveWatermark": true,
                "TemplateId": 1370613,
                "TemplateName": "victor0001"
            }
        ]
    }
}
```

