**Example 1: 开启告警**

开启告警

Input: 

```
tccli wedata ModifyBaselineAlarmStatus --cli-unfold-argument  \
    --IsAlarm true \
    --Id 24 \
    --ProjectId 1464962169590902784
```

Output: 
```
{
    "Response": {
        "Data": true,
        "RequestId": "34ef7381-4ccc-473d-b6da-81827752cde2"
    }
}
```

**Example 2: 编辑基线实例告警状态**

编辑基线实例告警状态

Input: 

```
tccli wedata ModifyBaselineAlarmStatus --cli-unfold-argument  \
    --IsAlarm true \
    --Id 35950 \
    --ProjectId 1470561602745229312
```

Output: 
```
{
    "Response": {
        "Data": true,
        "RequestId": "a33e309e-9341-44b7-a35f-b9645e737dac"
    }
}
```

**Example 3: 编辑状态**

编辑状态

Input: 

```
tccli wedata ModifyBaselineAlarmStatus --cli-unfold-argument  \
    --IsAlarm true \
    --Id 24 \
    --ProjectId 1464962169590902784
```

Output: 
```
{
    "Response": {
        "Data": true,
        "RequestId": "34ef7381-4ccc-473d-b6da-81827752cde2"
    }
}
```

