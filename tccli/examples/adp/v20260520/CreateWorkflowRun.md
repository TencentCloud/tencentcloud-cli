**Example 1: 创建工作流运行实例**

创建工作流运行实例

Input: 

```
tccli adp CreateWorkflowRun --cli-unfold-argument  \
    --AppId 2075134221221714816 \
    --Domain 1 \
    --Query 我想买车
```

Output: 
```
{
    "Response": {
        "CreateTime": "1784010161430",
        "WorkflowRunId": "wfr-cdcp9hyus1ds",
        "RequestId": "9c2def7a-ebdd-45cd-ada5-2898de26bd1d"
    }
}
```

