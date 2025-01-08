**Example 1: 查询实例的维护时间窗口**

查询	postgres-rwwbeuyx实例的维护窗口

Input: 

```
tccli postgres DescribeMaintainTimeWindow --cli-unfold-argument  \
    --DBInstanceId postgres-rwwbeuyx
```

Output: 
```
{
    "Response": {
        "DBInstanceId": "postgres-rwwbeuyx",
        "MaintainDuration": 1,
        "MaintainStartTime": "04:00",
        "MaintainWeekDays": [
            "monday",
            "tuesday",
            "wednesday",
            "thursday",
            "friday",
            "saturday",
            "sunday"
        ],
        "RequestId": "0f6113e2-f27c-4fe2-a63c-a298f4071e6c"
    }
}
```

