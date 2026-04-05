**Example 1: dev_test**



Input: 

```
tccli wedata ListTaskExecutionStateEnums --cli-unfold-argument  \
    --WorkspaceId 1 \
    --WorkflowExecutionId exec_1001 \
    --Type 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "BizEnumInfos": [
                {
                    "Count": 1,
                    "LabelKey": "TERMINATING",
                    "LabelValue": "正在终止"
                }
            ]
        },
        "RequestId": "085a2d2b-fe8e-4e70-b031-1152a0eace97"
    }
}
```

