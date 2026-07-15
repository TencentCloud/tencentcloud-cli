**Example 1: 查询事件类型列表**



Input: 

```
tccli es DescribeEventInfoList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "EventTypeInfoList": [
            {
                "EventType": 1,
                "EventTypeName": "硬件异常"
            }
        ],
        "RequestId": "0b362957-37ba-43ce-804d-db77e7194cc2"
    }
}
```

