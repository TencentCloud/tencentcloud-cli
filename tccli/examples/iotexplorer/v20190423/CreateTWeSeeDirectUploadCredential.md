**Example 1: 创建 TWeSee COS 直传凭据**



Input: 

```
tccli iotexplorer CreateTWeSeeDirectUploadCredential --cli-unfold-argument  \
    --ProductId 4AHMY9X89Y \
    --DeviceName dev002 \
    --ServiceType VID_COMP \
    --ChannelId 0 \
    --CallbackId cb-n9sl1wur \
    --CustomId custom-id-123 \
    --DurationSeconds 86400 \
    --MaxInvokeCount 200 \
    --StorageRegion ap-guangzhou \
    --UploadMethod manifest
```

Output: 
```
{
    "Response": {
        "ExpiredTime": 1782809094,
        "SecretId": "AKIDbz4LQvqmLPyr9wHI2jo***********************i1cuAW8mbg5nd5HMUvjh26",
        "SecretKey": "sxuVY/Gx0MYKgcj***************vO+OWUsqrxFgU=",
        "StorageBucket": "twesee-input-test-1258344699",
        "StoragePath": "Direct/700000975417/019f128d-8cfa-774d-a195-5bc9f9e4e5d9/",
        "StorageRegion": "ap-guangzhou",
        "Token": "8tE1OzlWwpXFWOoHgaZIj8tkfxYrfMDa66eac88da6820056a20bdb1928cfe5050AXEPri_7vsnPiWB9dNtYuSXlxlCr1ziGfXw2OJm9HRUImer3rIMrqIX-qURjgfS85QYWk4w_3VGrH6ogH3iq9H-KlbnyTXPDaTjBkMsudFyhO7MYajMoaUZC*****************************************************************************************************************************************************************************************O8nplkBg1AbAldlJ-1nb-Hr-1pRSusV2k4qgDKjnp2-7gPD8Pmu2kqFDYyLY5fp8ktMj_r6ZBMPRso4kj_m1qSvdMKqmnlZbW1tJXLJ0ltJb1KLinCY8iGB_hFbj2AKorF_BSF30Bl47oDsHLvWivEVuVFX1yNSH2KdIdT7ZldmK97wLNZVISGwqY",
        "RequestId": "8be65a7a-cfc9-45f7-ac4c-3210cbfb48b6"
    }
}
```

