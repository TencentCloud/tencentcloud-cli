**Example 1: 修改维护时间窗口**

修改postgres-c4wtbx1f实例的维护时间窗口为每周一、周二的23:00-00:00

Input: 

```
tccli postgres ModifyMaintainTimeWindow --cli-unfold-argument  \
    --MaintainWeekDays tuesday monday \
    --MaintainDuration 1 \
    --DBInstanceId postgres-c4wtbx1f \
    --MaintainStartTime 23:00
```

Output: 
```
{
    "Response": {
        "RequestId": "0f6113e2-f27c-4fe2-a63c-a298f4071e6c"
    }
}
```

