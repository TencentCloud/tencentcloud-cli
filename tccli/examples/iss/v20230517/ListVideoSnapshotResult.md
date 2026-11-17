**Example 1: 成功**



Input: 

```
tccli iss ListVideoSnapshotResult --cli-unfold-argument  \
    --BeginTime 1769510374 \
    --EndTime 1769520374 \
    --ConfigId f044***1******************821df8a75d \
    --ChannelId 4150*******3***b***8*******b7acce0c0 \
    --Type 1 \
    --ImageUrlExpires 600 \
    --PageNumber 1 \
    --PageSize 20
```

Output: 
```
{
    "Response": {
        "Data": {
            "List": [],
            "PageNumber": 1,
            "PageSize": 20,
            "TotalCount": 0
        },
        "RequestId": "330d405e-cb45-43a8-8712-c9c9587290ed"
    }
}
```

