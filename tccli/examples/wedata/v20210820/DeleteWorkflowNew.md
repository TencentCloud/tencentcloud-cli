**Example 1: 删除工作流**



Input: 

```
tccli wedata DeleteWorkflowNew --cli-unfold-argument  \
    --WorkFlowId xx \
    --EnableNotify True \
    --DeleteMode True \
    --ProjectId 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "Result": true,
            "ErrorId": "1111",
            "ErrorDesc": "xxxx"
        },
        "RequestId": "xx"
    }
}
```

