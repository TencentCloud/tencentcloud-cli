**Example 1: 提交工作流范例**

提交工作流

Input: 

```
tccli wedata SubmitWorkflow --cli-unfold-argument  \
    --StartScheduling true \
    --WorkflowId 9e993c1d-0cd9-11ed-8e105ba60 \
    --VersionRemark aa \
    --ProjectId 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "TaskIds": [
                "20230629153735945",
                "20230629153757617",
                "20230703141549308"
            ],
            "Result": true,
            "ErrorDesc": null,
            "ErrorId": null
        },
        "RequestId": "1c56c530-b6c9-4976-afd4-3b96fa2bd6bd"
    }
}
```

