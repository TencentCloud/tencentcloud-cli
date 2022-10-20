**Example 1: 修改安全日志清理设置信息**



Input: 

```
tccli tcss ModifySecLogCleanSettingInfo --cli-unfold-argument  \
    --DayLimit 180 \
    --ReservesDeadline 60 \
    --ReservesLimit 80
```

Output: 
```
{
    "Response": {
        "RequestId": "29b37d86-f63d-43d1-b21a-640e82965198"
    }
}
```

