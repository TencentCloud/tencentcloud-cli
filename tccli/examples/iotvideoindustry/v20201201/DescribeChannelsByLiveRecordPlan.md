**Example 1: 根据直播录制计划获取频道列表**



Input: 

```
tccli iotvideoindustry DescribeChannelsByLiveRecordPlan --cli-unfold-argument  \
    --PlanId plan-001
```

Output: 
```
{
    "Response": {
        "RequestId": "1",
        "TotalCount": 1,
        "LiveChannels": [
            {
                "ChannelId": "id0"
            }
        ]
    }
}
```

