**Example 1: 触发事件**

触发事件

Input: 

```
tccli wedata TriggerDsEvent --cli-unfold-argument  \
    --ProjectId 1470547050521227264 \
    --EventCaseList.0.Name myTest \
    --EventCaseList.0.Dimension 20220729 \
    --EventCaseList.0.Description 手动触发
```

Output: 
```
{
    "Response": {
        "Data": {
            "TotalCount": 1,
            "SuccessCount": 1,
            "FailCount": 0,
            "FailMessageList": []
        },
        "RequestId": "a339e515-9f6c-46b1-a43a-587f1c39067c"
    }
}
```

