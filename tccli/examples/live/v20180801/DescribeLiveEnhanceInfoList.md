**Example 1: 请求示例**

查询直播增强用量明细。

Input: 

```
tccli live DescribeLiveEnhanceInfoList --cli-unfold-argument  \
    --StartTime 2024-12-24T10:43:22+08:00 \
    --EndTime 2024-12-25T10:43:22+08:00 \
    --Granularity 0 \
    --DomainNames 5000.livepull.stream.com \
    --Type SUPER_RESOLUTION \
    --Resolution 720P \
    --Fps 30
```

Output: 
```
{
    "Response": {
        "DataInfoList": [
            {
                "Domain": "5000.livepull.stream.com",
                "Time": "2024-12-25T10:43:22+08:00",
                "Duration": 0,
                "Fps": "30",
                "Resolution": "720P",
                "Type": "SUPER_RESOLUTION"
            }
        ],
        "RequestId": "1047d0dc-6dc8-4898-a7f3-03726a822b0e"
    }
}
```

