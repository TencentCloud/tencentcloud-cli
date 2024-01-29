**Example 1: 示例1**

demo

Input: 

```
tccli wedata RenewWorkflowSchedulerInfoDs --cli-unfold-argument  \
    --ProjectId 1460947878944567296 \
    --WorkflowId e5b0945c-ed6d-11ed-8909-bc97e105ba60 \
    --DelayTime 0 \
    --SelfDepend serial \
    --StartTime 2023-05-13 12:44:29 \
    --EndTime 2023-05-12 23:59:59 \
    --TaskAction  \
    --CycleType DAY_CYCLE \
    --CycleStep 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "Failed": 0,
            "Success": 0,
            "Total": 0
        },
        "RequestId": "59a4462b-66f3-4cc2-80a2-46c416726c46"
    }
}
```

