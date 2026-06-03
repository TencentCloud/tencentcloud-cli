**Example 1: 视频语义搜索**



Input: 

```
tccli iotexplorer InvokeAISearchService --cli-unfold-argument  \
    --ProductId 4AHMY9X89Y \
    --DeviceName dev20260428a \
    --Query 有人走过
```

Output: 
```
{
    "Response": {
        "Summary": "共1段视频：雨后路滑，浅色路人正小心行走。安全起见，请防滑慢行哦！",
        "Targets": [
            {
                "ChannelId": 0,
                "DeviceName": "dev20260428a",
                "EndTimeMs": 1777357077918,
                "EventId": "_sys_id1_data",
                "Id": "019dd2bc-baa9-70ff-acd3-b7e88473c32d_1",
                "ProductId": "4AHMY9X89Y",
                "StartTimeMs": 1777357076918,
                "Summary": "穿浅色衣物的人在雨后湿滑的路边行走",
                "Thumbnail": "/700000975417/4AHMY9X89Y/dev20260428a/events/1777357076.jpg"
            }
        ],
        "VideoURL": "https://1259367869.vod2.myqcloud.com/timeshift/live/dev20260428a/timeshift.m3u8",
        "RequestId": "5485cc1a-5c7a-4d86-98f9-da7bba179f6c"
    }
}
```

**Example 2: 视频语义搜索（英文）**



Input: 

```
tccli iotexplorer InvokeAISearchService --cli-unfold-argument  \
    --ProductId 4AHMY9X89Y \
    --DeviceName dev20260428en \
    --Query person walking \
    --SummaryLang en-US
```

Output: 
```
{
    "Response": {
        "Summary": "1 video shows a person walking safely on a wet sidewalk after rain. Stay cautious on slippery paths!",
        "Targets": [
            {
                "ChannelId": 0,
                "DeviceName": "dev20260428en",
                "EndTimeMs": 1777356974727,
                "EventId": "",
                "Id": "019dd2bb-273c-7a95-bf08-8da22f56f415_1",
                "ProductId": "4AHMY9X89Y",
                "StartTimeMs": 1777356973727,
                "Summary": "A person in light-colored clothes walking on a wet and slippery roadside after the rain",
                "Thumbnail": "/700000975417/4AHMY9X89Y/dev20260428en/events/1777356973.jpg"
            }
        ],
        "VideoURL": "https://1259367869.vod2.myqcloud.com/timeshift/live/dev20260428en/timeshift.m3u8",
        "RequestId": "b91d707d-bb24-40e8-8887-1984a58de77a"
    }
}
```

**Example 3: 视频语义搜索（结果按时间升序排序）**



Input: 

```
tccli iotexplorer InvokeAISearchService --cli-unfold-argument  \
    --ProductId 4AHMY9X89Y \
    --DeviceName dev20260426 \
    --Query 今天的视频 \
    --Order TIME_ASC
```

Output: 
```
{
    "Response": {
        "Summary": "共2段视频：雨后湿滑路面行人慢行，蓝色货车弯道行驶。雨天路滑，请注意交通安全哦！",
        "Targets": [
            {
                "ChannelId": 0,
                "DeviceName": "dev20260426",
                "EndTimeMs": 1777212005402,
                "EventId": "",
                "Id": "019dca17-1c33-7650-8294-bb99e524059b_1",
                "ProductId": "4AHMY9X89Y",
                "StartTimeMs": 1777212005402,
                "Summary": "穿浅色衣物的人在雨后湿滑的路边行走",
                "Thumbnail": "/700000975417/4AHMY9X89Y/dev20260426/events/1777212005.jpg"
            }
        ],
        "VideoURL": "https://1259367869.vod2.myqcloud.com/timeshift/live/dev20260426/timeshift.m3u8",
        "RequestId": "6e9d71e1-b778-415d-a276-59de83ecab97"
    }
}
```

