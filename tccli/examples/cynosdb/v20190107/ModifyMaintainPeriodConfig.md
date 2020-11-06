**Example 1: 修改实例维护时间窗**



Input: 

```
tccli cynosdb ModifyMaintainPeriodConfig --cli-unfold-argument  \
    --InstanceId cynosdbpg-ins-n7ocdslw \
    --MaintainStartTime 3600 \
    --MaintainDuration 3600 \
    --MaintainWeekDays '[Mon, Tue]'
```

Output: 
```
{
    "Response": {
        "RequestId": "165202"
    }
}
```

