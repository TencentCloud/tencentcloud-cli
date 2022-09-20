**Example 1: 查询DDoS封禁解封列表**



Input: 

```
tccli teo DescribeDDoSBlockList --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0 \
    --PolicyIds 1705 \
    --EventIds 1231412451 \
    --ZoneIds zone-21xfqlh4qjee \
    --StartTime 2020-09-22T00:00:00+00:00 \
    --Area overseas
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RequestId": "a79e60f8-34cc-4ee5-a7f9-a24adb572c68",
        "Data": [
            {
                "EndTime": 1660010400,
                "StartTime": 1660010700
            }
        ]
    }
}
```

