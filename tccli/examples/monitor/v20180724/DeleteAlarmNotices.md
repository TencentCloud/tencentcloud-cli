**Example 1: 删除告警通知模板（批量）**

删除两个告警通知模板

Input: 

```
tccli monitor DeleteAlarmNotices --cli-unfold-argument  \
    --Module monitor \
    --NoticeIds notice-235h325y notice-h25hj534h
```

Output: 
```
{
    "Response": {
        "RequestId": "fahkjbgag3h2bvaqer2-23"
    }
}
```

