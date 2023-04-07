**Example 1: 示例**

获取时间范围内所有告警vid

Input: 

```
tccli cwp DescribeAlarmVertexId --cli-unfold-argument  \
    --Uuid abc \
    --StartTime 0 \
    --EndTime 0
```

Output: 
```
{
    "Response": {
        "AlarmVertexIds": [
            "abc"
        ],
        "RequestId": "abc"
    }
}
```

