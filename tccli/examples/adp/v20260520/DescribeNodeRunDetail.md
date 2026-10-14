**Example 1: 查看工作流节点运行详情**

查看工作流节点运行详情

Input: 

```
tccli adp DescribeNodeRunDetail --cli-unfold-argument  \
    --AppId 2075134221221714816 \
    --NodeRunId nr-9b1b61e9-b4a5-46a7-80b6-89da1c71db00
```

Output: 
```
{
    "Response": {
        "NodeRunDetail": {
            "NodeRun": {
                "BranchIndexList": [],
                "FailCode": "",
                "FailMessage": "",
                "NodeId": "d63dfc51-bdc1-721c-0a4b-0be14f75bd62",
                "NodeName": "参数提取1",
                "NodeRunId": "nr-9b1b61e9-b4a5-46a7-80b6-89da1c71db00",
                "NodeType": 2,
                "Status": 3,
                "TotalCostMs": 60704,
                "TotalTokens": 1647,
                "WorkflowRunId": "wfr-cd6a2j03k5j4"
            },
            "NodeRunContent": {
                "Input": "{\"对话历史\":\"用户输入：我想买车\\n机器人回答：请问您想买什么品牌的汽车？\",\"当前时间\":\"今天是2026年07月13日，星期一。现在时间是：下午4点47分\",\"用户本轮对话内容\":\"买奇瑞汽车\"}",
                "InputRef": "",
                "OriginalOutput": "",
                "OriginalOutputRef": "",
                "Output": "{\"汽车品牌\":\"奇瑞\"}",
                "OutputRef": ""
            },
            "NodeRunExecution": {
                "BatchRunSummary": null,
                "EndTime": "1783932471280",
                "StartTime": "1783932410575"
            },
            "NodeRunLog": {
                "Log": "",
                "LogRef": ""
            },
            "StatisticList": [
                {
                    "FirstTokenCostMs": 0,
                    "InputTokens": 1529,
                    "ModelName": "workflow-light-32b",
                    "OutputTokens": 118,
                    "TotalCostMs": 0,
                    "TotalTokens": 1647
                }
            ]
        },
        "RequestId": "6228826a-b0c2-4a58-8597-a7a09e46f2b3"
    }
}
```

