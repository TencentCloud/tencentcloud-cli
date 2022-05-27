**Example 1: 修改实例维护时间窗**



Input: 

```
tccli cynosdb ModifyMaintainPeriodConfig --cli-unfold-argument  \
    --InstanceId cynosdbmysql-ins-n7ocdslw \
    --MaintainStartTime 3600 \
    --MaintainDuration 3600 \
    --MaintainWeekDays Mon
```

Output: 
```
{
    "Response": {
        "RequestId": "165202"
    }
}
```

