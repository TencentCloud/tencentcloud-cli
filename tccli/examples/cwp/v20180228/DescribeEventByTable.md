**Example 1: 示例**

根据事件表名和id查询告警事件详情

Input: 

```
tccli cwp DescribeEventByTable --cli-unfold-argument  \
    --TableName events_bash \
    --Ids 0
```

Output: 
```
{
    "Response": {
        "Type": "bash",
        "Value": "value",
        "RequestId": "xxxxxxxx-1234-5678-9101-yyyyyyyyyy"
    }
}
```

