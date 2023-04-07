**Example 1: 示例**

根据事件表名和id查询告警事件详情

Input: 

```
tccli cwp DescribeEventByTable --cli-unfold-argument  \
    --TableName abc \
    --Ids 0
```

Output: 
```
{
    "Response": {
        "Type": "abc",
        "Value": "abc",
        "RequestId": "abc"
    }
}
```

