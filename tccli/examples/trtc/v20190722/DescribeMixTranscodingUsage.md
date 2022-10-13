**Example 1: 获取用户在2022年1月1日-2022年1月2日范围内，SdkAppId为1400123456的应用的用量明细。**



Input: 

```
tccli trtc DescribeMixTranscodingUsage --cli-unfold-argument  \
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
            "SDH264",
            "HDH264",
            "FullHDH264",
            "2KH264",
            "4KH264",
            "SDH265",
            "HDH265",
            "FullHDH265",
            "2KH265",
            "4KH265"
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
                    60,
                    70,
                    80,
                    90,
                    100,
                    110
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
                    60,
                    70,
                    80,
                    90,
                    100,
                    110
                ]
            }
        ],
        "RequestId": "xx"
    }
}
```

