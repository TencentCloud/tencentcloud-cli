**Example 1: 修改应用采样率**



Input: 

```
tccli rum ModifyTDEMSampleRate --cli-unfold-argument  \
    --AppId 11 \
    --SampleRate 50 \
    --ReplaySampleRate 50
```

Output: 
```
{
    "Response": {
        "AppId": "11",
        "ReplaySampleRate": 50,
        "SampleRate": 50,
        "UpdatedAt": "2026-09-22 11:35:51",
        "RequestId": "09c24f77-a3e3-4d56-a4b2-49db017bdc55"
    }
}
```

