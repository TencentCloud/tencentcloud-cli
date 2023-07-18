**Example 1: 下载声音复刻离线模型**

下载声音复刻离线模型

Input: 

```
tccli vrs DownloadVRSModel --cli-unfold-argument  \
    --TaskId efe36c79-1c71-41d1-b541-04075fb3b9aa
```

Output: 
```
{
    "Response": {
        "Data": {
            "Model": "https://xxx-xxx-xxxx.cos.ap-guangzhou.myqcloud.com/xxxx.zip",
            "VoiceName": "a",
            "VoiceGender": 1,
            "VoiceLanguage": 1,
            "TaskId": "efe36c79-1c71-41d1-b541-04075fb3b9aa"
        },
        "RequestId": "3ccdce8-15d7-4536-9325-8259266c21"
    }
}
```

