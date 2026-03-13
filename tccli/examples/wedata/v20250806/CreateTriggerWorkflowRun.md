**Example 1: 工作流执行自定义参数执行**



Input: 

```
tccli wedata CreateTriggerWorkflowRun --cli-unfold-argument  \
    --ProjectId 3126203***945134080 \
    --WorkflowId 9f551833-215***772-8ec1-78019779617c \
    --AdvancedParams.0.ParamKey k1 \
    --AdvancedParams.0.ParamValue k2 \
    --TaskIds 202601***53102448 \
    --SchedulingResourceGroupId 2026010***5230846836 \
    --IntegrationResourceGroupId 2025062***2930469737
```

Output: 
```
{
    "Response": {
        "Data": {
            "WorkflowExecutionId": "74fe7410-a820-42ea-80ea-06eb793d06c2"
        },
        "RequestId": "164284d1-4205-4883-bcff-2c1ee5f38764"
    }
}
```

