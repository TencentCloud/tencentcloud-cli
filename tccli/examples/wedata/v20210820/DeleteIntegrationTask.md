**Example 1: 删除集成任务**

删除集成任务

Input: 

```
tccli wedata DeleteIntegrationTask --cli-unfold-argument  \
    --ProjectId 123 \
    --TaskId 345
```

Output: 
```
{
    "Response": {
        "Data": true,
        "DeleteFlag": 0,
        "DeleteErrInfo": "abc",
        "RequestId": "abc"
    }
}
```

