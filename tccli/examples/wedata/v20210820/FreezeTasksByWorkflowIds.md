**Example 1: 暂停工作流下的所有任务--暂停成功**

暂停工作流下的所有任务--暂停成功

Input: 

```
tccli wedata FreezeTasksByWorkflowIds --cli-unfold-argument  \
    --WorkflowIds e1c0831c-e1a3-11ee-8ec8-b8599f277de5 \
    --ProjectId 1470547050521227264
```

Output: 
```
{
    "Response": {
        "Data": {
            "ErrorDesc": null,
            "ErrorId": null,
            "Result": true,
            "ResultMsg": null
        },
        "RequestId": "ba5bafa6-e05d-4877-8f2e-0de7cc00305c"
    }
}
```

