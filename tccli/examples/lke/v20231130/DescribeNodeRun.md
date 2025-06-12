**Example 1: 查看工作流异步运行实例的节点的运行详情**

已经创建了工作流异步运行实例，通过DescribeWorkflowRun接口获取到节点的基本信息，再通过此接口可获取节点的运行详情

Input: 

```
tccli lke DescribeNodeRun --cli-unfold-argument  \
    --NodeRunId n223-4358-b8a0-b4d65712f44c
```

Output: 
```
{
    "Response": {
        "NodeRun": {
            "NodeRunId": "nf5a21-6223-4358-b8a789",
            "NodeId": "e60de932-b050-65ce-261e-027760e93d81",
            "WorkflowRunId": "1dcf5a21-6223-4358-b8a0-b4d6",
            "NodeName": "大模型节点",
            "NodeType": 3,
            "State": 1,
            "FailCode": "",
            "FailMessage": "",
            "CostMilliseconds": 1000,
            "TotalTokens": 100,
            "Input": "{\"Age\": 12}",
            "InputRef": "",
            "Output": "{\"Age\": 12}",
            "OutputRef": "",
            "TaskOutput": "{\"Age\": 12...",
            "TaskOutputRef": "https://lke-realtime-test-1251316161.cos.ap-guangzhou.myqcloud.com/xxxx/xxxx.json",
            "Log": "",
            "LogRef": "",
            "StartTime": "1672531200000",
            "EndTime": "1672531300000",
            "StatisticInfos": [
                {
                    "ModelName": "workflow-pro",
                    "FirstTokenCost": 200,
                    "TotalCost": 1000,
                    "InputTokens": 20,
                    "OutputTokens": 30,
                    "TotalTokens": 50
                }
            ]
        },
        "RequestId": "925208e7-46fa-43b3-a429-ddcbccad24f6"
    }
}
```

