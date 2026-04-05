**Example 1: 示例1**



Input: 

```
tccli wedata CreateStreamTask --cli-unfold-argument  \
    --WorkspaceId id_1 \
    --TaskInfo.TaskName test_name_1 \
    --TaskInfo.TaskId test_id_1
```

Output: 
```
{
    "Response": {
        "Data": {
            "TaskId": "ec438445-aeca-4859-8610-05e83ba6dc06"
        },
        "RequestId": "b7da2148-9a1f-465e-8a2a-1b68327177a7"
    }
}
```

