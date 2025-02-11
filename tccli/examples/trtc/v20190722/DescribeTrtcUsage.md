**Example 1: 获取用户在2022年1月1日-2022年1月2日范围内，SdkAppId为1400123456的应用的用量明细。**



Input: 

```
tccli trtc DescribeTrtcUsage --cli-unfold-argument  \
    --EndTime 2022-01-01 \
    --StartTime 2022-01-02 \
    --SdkAppId 1400123456
```

Output: 
```
{
    "Response": {
        "UsageKey": [
            "Audio",
            "SD",
            "HD",
            "FullHD",
            "2K",
            "4K"
        ],
        "UsageList": [
            {
                "TimeKey": "2022-01-01 00:00:00",
                "UsageValue": [
                    10,
                    20,
                    30,
                    40,
                    50,
                    60
                ]
            },
            {
                "TimeKey": "2022-01-02 00:00:00",
                "UsageValue": [
                    10,
                    20,
                    30,
                    40,
                    50,
                    60
                ]
            }
        ],
        "RequestId": "635e1617-0613-4bf8-8f1f-e017754713e8"
    }
}
```

