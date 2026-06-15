**Example 1: 查询游戏专区指定游戏的近期公告列表**



Input: 

```
tccli lighthouse DescribeAnnouncements --cli-unfold-argument  \
    --Filters.0.Name blueprint-id \
    --Filters.0.Values lhbp-o2ra0yxx \
    --Filters.1.Name announcement-type \
    --Filters.1.Values RECENT \
    --Filters.2.Name display-area \
    --Filters.2.Values GAME_PORTAL \
    --Offset 0 \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "RequestId": "e9bad65d-809b-4851-b3c1-5015730a726c",
        "TotalCount": 15,
        "AnnouncementSet": [
            {
                "AnnouncementId": "lhanno-00000097",
                "Title": "游戏更新公告",
                "Content": "服务已恢复，给您带来不便深表歉意。",
                "AnnouncementType": "RECENT",
                "AnnouncementState": "ONELINE",
                "AnnouncementTagSet": [
                    "游戏更新",
                    "系统维护"
                ],
                "CreatedTime": "2025-07-15T00:11:18+08:00",
                "AnnouncementTime": "2025-07-15T00:11:18+08:00",
                "Read": false
            }
        ]
    }
}
```

