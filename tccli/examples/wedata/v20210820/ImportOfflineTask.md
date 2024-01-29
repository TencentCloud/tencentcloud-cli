**Example 1: 集成导入接口**

集成导入接口

Input: 

```
tccli wedata ImportOfflineTask --cli-unfold-argument  \
    --ProjectId abc \
    --TaskInfoList.0.TaskId abc \
    --TaskInfoList.0.TaskName abc \
    --TaskNameExistMode 0 \
    --WorkflowId abc \
    --TaskFolderId abc
```

Output: 
```
{
    "Response": {
        "Data": 0,
        "RequestId": "abc"
    }
}
```

