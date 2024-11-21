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
        "RequestId": "acdd5474-6360-4fd4-bfc7-843162cb8116"
    }
}
```

