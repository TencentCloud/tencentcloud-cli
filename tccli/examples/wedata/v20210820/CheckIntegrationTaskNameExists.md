**Example 1: CheckIntegrationTaskNameExists**

判断集成任务名称是否存在

Input: 

```
tccli wedata CheckIntegrationTaskNameExists --cli-unfold-argument  \
    --ProjectId abc \
    --TaskName abc \
    --TaskId abc
```

Output: 
```
{
    "Response": {
        "Data": true,
        "ExistsType": 1,
        "RequestId": "abc"
    }
}
```

