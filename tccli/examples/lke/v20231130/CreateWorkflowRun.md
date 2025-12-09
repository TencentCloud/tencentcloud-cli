**Example 1: 创建工作流的异步运行实例**

针对运行时间比较长的工作流的场景。步骤：在平台上创建好符合条件（不含参数提取节点、选项卡节点和回复节点）的工作流并调试通过，编辑应用设置成“单工作流模式”，选择工作流，打开“异步调用”的开关，然后再调用本接口。

Input: 

```
tccli lke CreateWorkflowRun --cli-unfold-argument  \
    --RunEnv 1 \
    --AppBizId 1854548189164339200 \
    --Query 发起任务 \
    --CustomVariables.0.Name name \
    --CustomVariables.0.Value 张三
```

Output: 
```
{
    "Response": {
        "RequestId": "42c23cf3-0dbb-4676-a5a0-bb9cb0787f5d",
        "AppBizId": "1854548189164339200",
        "WorkflowRunId": "67c23cf3-077b-4644-225a0-bb9cb078322",
        "RunEnv": 1,
        "CreateTime": "1672531200000",
        "Query": "发起任务",
        "CustomVariables": [
            {
                "Name": "name",
                "Value": "张三"
            }
        ]
    }
}
```

