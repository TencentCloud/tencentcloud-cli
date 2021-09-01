**Example 1: 获取统计数据**



Input: 

```
tccli ses GetStatisticsReport --cli-unfold-argument  \
    --Domain qcloud.com \
    --StartDate 2020-10-01 \
    --EndDate 2020-10-03 \
    --ReceivingMailboxType gmail.com
```

Output: 
```
{
    "Response": {
        "RequestId": "8979fc1e-9564-4fc9-bf7d-2958ce679b72",
        "DailyVolumes": [
            {
                "SendDate": "2020-10-01",
                "RequestCount": 1000,
                "AcceptedCount": 999,
                "DeliveredCount": 998,
                "OpenedCount": 300,
                "ClickedCount": 199,
                "BounceCount": 5,
                "UnsubscribeCount": 1
            }
        ],
        "OverallVolume": {
            "SendDate": "2020-10-01",
            "RequestCount": 1000,
            "AcceptedCount": 999,
            "DeliveredCount": 998,
            "OpenedCount": 300,
            "ClickedCount": 199,
            "BounceCount": 5,
            "UnsubscribeCount": 1
        }
    }
}
```

