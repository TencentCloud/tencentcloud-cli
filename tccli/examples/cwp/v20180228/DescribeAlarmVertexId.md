**Example 1: 示例**

获取时间范围内所有告警vid

Input: 

```
tccli cwp DescribeAlarmVertexId --cli-unfold-argument  \
    --Uuid 1c26308c-5493-4eaf-a817-112ec25f499e \
    --StartTime 0 \
    --EndTime 0
```

Output: 
```
{
    "Response": {
        "AlarmVertexIds": [
            "23eeeb4347bdd26bfc6b7ee9a3b755dd"
        ],
        "RequestId": "xxxxxxxx-1234-5678-9101-yyyyyyyyyy"
    }
}
```

