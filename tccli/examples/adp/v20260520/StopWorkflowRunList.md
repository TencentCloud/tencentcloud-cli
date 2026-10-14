**Example 1: 批量停止工作流运行实例**

批量停止工作流运行实例

Input: 

```
tccli adp StopWorkflowRunList --cli-unfold-argument  \
    --AppId 2075134221221714816 \
    --WorkflowRunIdList wfr-cd6a2j03k5j4
```

Output: 
```
{
    "Response": {
        "FailedIdList": [],
        "SuccessIdList": [
            "wfr-cd6a2j03k5j4"
        ],
        "RequestId": "c126301e-91a7-433c-9b21-a543a03c513f"
    }
}
```

