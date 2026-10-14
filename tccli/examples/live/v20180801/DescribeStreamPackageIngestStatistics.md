**Example 1: 请求示例**



Input: 

```
tccli live DescribeStreamPackageIngestStatistics --cli-unfold-argument  \
    --StartTime 2026-09-23T00:00:00+08:00 \
    --EndTime 2026-09-24T00:00:00+08:00 \
    --ChannelIds 68774AEC000027733C4C \
    --Types LiveChannel \
    --Dimension True \
    --Granularity 5
```

Output: 
```
{
    "Response": {
        "DataInfoList": [
            {
                "ChannelId": "68774AEC000027733C4C",
                "Ingest": 137081471,
                "Time": "2026-09-23T00:00:00+08:00",
                "Type": "LiveChannel"
            }
        ],
        "TotalIngest": 37788778885,
        "RequestId": "22ffc5ce-b418-4bb8-b8a8-9c1c413e55b3"
    }
}
```

