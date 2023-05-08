**Example 1: 实例批量置成功**



Input: 

```
tccli wedata ForceSucInstances --cli-unfold-argument  \
    --Instances.0.TaskId 123 \
    --Instances.0.CurRunDate 2022-08-04 00:00:00 \
    --ProjectId 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "ErrorDesc": "数据库操作失败",
            "Result": true,
            "ErrorId": "111"
        },
        "RequestId": "xx"
    }
}
```

