**Example 1: 搜索事件列表**



Input: 

```
tccli rum DescribeTDEMEventSearch --cli-unfold-argument  \
    --AppId 7 \
    --StartTime 1787404860000 \
    --EndTime 1789996860000 \
    --Category lag
```

Output: 
```
{
    "Response": {
        "Events": [
            {
                "AppVersion": "1.0.4",
                "Browser": "***%**C**es",
                "City": "北京",
                "Country": "中国",
                "DeviceType": "iPhone18,1",
                "EventCategory": "performance",
                "EventId": "33C06D53-C870-4276-8942-D8A970D16475",
                "EventProperties": [
                    {
                        "Key": "app_state",
                        "Value": "active"
                    }
                ],
                "EventType": "lag_detected",
                "ExceptionStacks": [
                    {
                        "MechanismHandled": 1,
                        "MechanismType": "hybrid_frame_watchdog",
                        "Type": "MainThreadStall",
                        "Value": "main_thread_unresponsive"
                    }
                ],
                "Ip": "223.******.23",
                "Isp": "移动/基站WiFi",
                "Measurements": [
                    {
                        "Key": "cumulative_frame_delay_ms",
                        "Value": 150.024917
                    }
                ],
                "NormalizedPageUrl": "launch",
                "Os": "iOS",
                "PageUrl": "launch",
                "Platform": "ios",
                "Province": "北京",
                "SessionId": "8B771143-FC48-4E11-B3BC-E328A2337CBC",
                "Timestamp": 1789636841337,
                "UserId": "tdem_test_2ab8d5"
            }
        ],
        "Page": 1,
        "PageSize": 20,
        "Total": 3410,
        "RequestId": "c3971020-ac30-49f0-a02c-8942700aaa43"
    }
}
```

