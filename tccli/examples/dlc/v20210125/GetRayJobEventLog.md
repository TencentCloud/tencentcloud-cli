**Example 1: 获取作业事件日志**



Input: 

```
tccli dlc GetRayJobEventLog --cli-unfold-argument  \
    --Id rayjob-1773632068-nksg \
    --StartTime 1773625164000 \
    --EndTime 1773635964000 \
    --Page 1 \
    --PageSize 2 \
    --SortFields.0.Field StartTime \
    --SortFields.0.Order asc
```

Output: 
```
{
    "Response": {
        "Events": [
            {
                "Component": "RayJob",
                "EventTime": 1773632143,
                "Level": "INFO",
                "Message": "Job is running on remote cluster"
            }
        ],
        "Page": 1,
        "PageSize": 2,
        "TotalCount": 2,
        "TotalPages": 1,
        "RequestId": "9bb194f1-6454-4818-93a3-bd926b9ef814"
    }
}
```

