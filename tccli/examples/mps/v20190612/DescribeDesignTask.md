**Example 1: 查询音色设计结果**



Input: 

```
tccli mps DescribeDesignTask --cli-unfold-argument  \
    --TaskId 1300057393-DesignVoiceAsync-88434eca-1484-4fcc-8589-e98027fc174e
```

Output: 
```
{
    "Response": {
        "ErrorCode": 0,
        "Msg": "success",
        "Status": "success",
        "VoiceId": "v1_kuuEfwa/ADAozD26I/1sVcQgNNNj0egjBFWrvjnyqiaXzF8qfejCmOlUQc8n5Ss+CoRyMoYOrD3o9E0=",
        "RequestId": "5bf0e591-fadc-4b5f-9c9a-9586e09ec6af"
    }
}
```

**Example 2: 查询音色设计（带预览）结果**



Input: 

```
tccli mps DescribeDesignTask --cli-unfold-argument  \
    --TaskId 1300057393-DesignVoiceAsync-0ce1e964-516d-490a-80e2-1c8f574fd493
```

Output: 
```
{
    "Response": {
        "AudioUrl": "https://laurie-tmp-1300828900.cos.ap-nanjing.myqcloud.com/async_dubbing/0ce1e964-516d-490a-80e2-1c8f574fd493-preview.mp3",
        "ErrorCode": 0,
        "Msg": "success",
        "Status": "success",
        "VoiceId": "v1_zzXhFVNQhPxEP5OEFCa5K1xS1T7tndirMHTN/RCm+nx/cqsSqdsCqzHe3rxHo16e8m026KhWTtt/HUY=",
        "RequestId": "0ec0f8a6-299b-43c0-a528-9dcd8eaf340a"
    }
}
```

