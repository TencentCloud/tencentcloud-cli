**Example 1: 查询互动白板时长用量**

查询2021-09-01到2021-09-07的互动白板时长用量

Input: 

```
tccli tiw DescribeTIWDailyUsage --cli-unfold-argument  \
    --SdkAppId 1400000001 \
    --SubProduct sp_tiw_board \
    --StartTime 2021-09-01 \
    --EndTime 2021-09-07
```

Output: 
```
{
    "Response": {
        "RequestId": "cdfb2097-75d1-4159-ad37-62d9eca65d6a",
        "Usages": [
            {
                "Time": "2021-09-01",
                "SdkAppId": 1400000001,
                "SubProduct": "sp_tiw_board",
                "Value": 779552
            },
            {
                "Time": "2021-09-02",
                "SdkAppId": 1400000001,
                "SubProduct": "sp_tiw_board",
                "Value": 78118
            },
            {
                "Time": "2021-09-03",
                "SdkAppId": 1400000001,
                "SubProduct": "sp_tiw_board",
                "Value": 768385
            },
            {
                "Time": "2021-09-04",
                "SdkAppId": 1400000001,
                "SubProduct": "sp_tiw_board",
                "Value": 94257
            },
            {
                "Time": "2021-09-05",
                "SdkAppId": 1400000001,
                "SubProduct": "sp_tiw_board",
                "Value": 26717
            },
            {
                "Time": "2021-09-06",
                "SdkAppId": 1400000001,
                "SubProduct": "sp_tiw_board",
                "Value": 95296
            },
            {
                "Time": "2021-09-07",
                "SdkAppId": 1400000001,
                "SubProduct": "sp_tiw_board",
                "Value": 70592
            }
        ]
    }
}
```

