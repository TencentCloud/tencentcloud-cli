**Example 1: 调用示例**

查询线性组装频道用量信息

Input: 

```
tccli mps DescribeStreamPackageLinearAssemblyUsage --cli-unfold-argument  \
    --StartTime 2026-02-10T11:00:00+08:00 \
    --EndTime 2026-02-10T11:20:00+08:00 \
    --Dimension False \
    --ChannelIds 698A9F401D3EA6831FD9 \
    --ChannelTiers Standard
```

Output: 
```
{
    "Response": {
        "Info": {
            "AssemblyUsageDetails": [
                {
                    "ChannelID": "698A9F401D3EA6831FD9",
                    "ChannelName": "test_channel",
                    "ChannelTier": "Standard",
                    "Duration": 0
                }
            ],
            "SumBasicChannelDuration": 0,
            "SumStandardChannelDuration": 0
        },
        "RequestId": "84cb1a5a-9c26-4e3d-aabc-4f228e6136c5"
    }
}
```

