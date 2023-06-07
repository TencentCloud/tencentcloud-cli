**Example 1: 删除告警规则**

删除告警规则

Input: 

```
tccli wedata DeleteTaskAlarmRegular --cli-unfold-argument  \
    --ProjectId 123 \
    --Id 1
```

Output: 
```
{
    "Response": {
        "Data": true,
        "RequestId": "123"
    }
}
```

