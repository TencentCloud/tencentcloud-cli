**Example 1: 查询应用采样率**



Input: 

```
tccli rum DescribeTDEMSampleRate --cli-unfold-argument  \
    --AppId 11
```

Output: 
```
{
    "Response": {
        "AppId": "11",
        "CreatedAt": "2026-09-17 19:25:27",
        "ReplaySampleRate": 100,
        "SampleRate": 100,
        "UpdatedAt": "2026-09-17 19:25:27",
        "RequestId": "35d0085e-5d4a-4b64-a76d-ec8fffc8202e"
    }
}
```

