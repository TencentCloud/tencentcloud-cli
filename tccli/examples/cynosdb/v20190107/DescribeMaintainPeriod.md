**Example 1: 查询维护时间窗**



Input: 

```
tccli cynosdb DescribeMaintainPeriod --cli-unfold-argument  \
    --InstanceId cynosdbpg-ins-n7ocdslw
```

Output: 
```
{
    "Response": {
        "RequestId": "165202",
        "MaintainWeekDays": [
            "Mon",
            "Tue"
        ],
        "MaintainStartTime": "3600",
        "MaintainDuration": "3600"
    }
}
```

