**Example 1: 判断告警规则重名**



Input: 

```
tccli wedata CheckAlarmRegularNameExist --cli-unfold-argument  \
    --ProjectId xx \
    --AlarmRegularName xx \
    --TaskId xx
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "Data": true
    }
}
```

