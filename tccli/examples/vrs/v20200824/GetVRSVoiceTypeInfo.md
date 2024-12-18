**Example 1: 查询复刻音色信息**

查询复刻音色信息

Input: 

```
tccli vrs GetVRSVoiceTypeInfo --cli-unfold-argument  \
    --VoiceType 200000000 \
    --FastVoiceType c0be5744e9804c5fae5708fbd71db20d \
    --TaskType 5
```

Output: 
```
{
    "Response": {
        "Data": {
            "DateCreated": "2024-05-30T15:53:58+08:00",
            "ExpireTime": "2025-05-25T15:54:10+08:00",
            "FastVoiceType": "c0be5744e9804c5fae5708fbd71db20d",
            "IsDeployed": true,
            "TaskID": "fast6d467a51055149138f7fc8852dbd86a0",
            "TaskType": 5,
            "VoiceGender": 1,
            "VoiceName": "ceshi",
            "VoiceType": 200000000
        },
        "RequestId": "9bf903a9-437e-4448-b015-c3c920e2e9cc"
    }
}
```

