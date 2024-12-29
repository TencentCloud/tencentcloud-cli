**Example 1: 请求示例**



Input: 

```
tccli live DescribeLiveRecordTemplate --cli-unfold-argument  \
    --TemplateId 10000
```

Output: 
```
{
    "Response": {
        "RequestId": "3fefec28-3f95-4055-8a22-714cc271251e",
        "Template": {
            "AacParam": {
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
                "StorageTime": 123,
                "VodFileName": "",
                "VodSubAppId": 251006352
            },
            "FlvSpecialParam": {
                "UploadInRecording": true
            },
            "HlsParam": {
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
            "RemoveWatermark": true,
            "TemplateId": 1370613,
            "TemplateName": "victor0001"
        }
    }
}
```

