**Example 1: 查询工作流运行实例详情**

查询工作流运行实例详情

Input: 

```
tccli adp DescribeWorkflowRun --cli-unfold-argument  \
    --AppId 2075134221221714816 \
    --WorkflowRunId wfr-cd6a2j03k5j4
```

Output: 
```
{
    "Response": {
        "NodeRunList": [
            {
                "BranchIndexList": [],
                "FailCode": "",
                "FailMessage": "",
                "NodeId": "9e7966a3-43ad-378f-8586-8d5e107a0e2b",
                "NodeName": "开始",
                "NodeRunId": "nr-6f7aa512-f336-4ee1-b78e-a987f61ffd07",
                "NodeType": 1,
                "Status": 3,
                "TotalCostMs": 0,
                "TotalTokens": 0,
                "WorkflowRunId": "wfr-cd6a2j03k5j4"
            }
        ],
        "SubWorkflowNodePath": "",
        "WorkflowRun": {
            "WorkflowRunMetadata": {
                "CustomVariableList": [],
                "MainModelName": "Youtu/youtu-mrc-pro",
                "Query": "买奇瑞汽车",
                "WorkflowGraph": ""
            },
            "WorkflowRunOutput": {
                "LatestMessage": {
                    "ContentList": [
                        {
                            "FileCollection": null,
                            "OptionCardList": [],
                            "Text": "欢迎光临",
                            "Type": "text",
                            "Widget": null
                        }
                    ]
                },
                "Output": "{无}"
            },
            "WorkflowRunSummary": {
                "Domain": 1,
                "WorkflowRunProfile": {
                    "AppId": "2075134221221714816",
                    "Name": "买汽车",
                    "WorkflowId": "f5d9e1eb-d6c3-4529-93b1-f041ea3347cc",
                    "WorkflowRunId": "wfr-cd6a2j03k5j4"
                },
                "WorkflowRunResult": {
                    "FailMessage": "",
                    "Status": 3,
                    "TotalTokens": 1647
                },
                "WorkflowRunTime": {
                    "CreateTime": "1783932410370",
                    "EndTime": "1783932471294",
                    "StartTime": "1783932410478"
                }
            }
        },
        "RequestId": "461b7bb7-ded9-4f02-814e-afb07ee4ffb7"
    }
}
```

