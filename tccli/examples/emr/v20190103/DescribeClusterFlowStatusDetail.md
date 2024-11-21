**Example 1: 查询EMR任务运行详情状态**



Input: 

```
tccli emr DescribeClusterFlowStatusDetail --cli-unfold-argument  \
    --InstanceId emr-123 \
    --FlowParam.FKey TraceId \
    --FlowParam.FValue 1730204629-375383-1016312 \
    --NeedExtraDetail True
```

Output: 
```
{
    "Response": {
        "FlowDesc": [
            {
                "PKey": "CoreSize",
                "PValue": "1"
            },
            {
                "PKey": "DeployProcess",
                "PValue": "DataNode,NodeManager,Filebeat"
            },
            {
                "PKey": "Node Type",
                "PValue": "Core"
            }
        ],
        "FlowExtraDetail": null,
        "FlowName": "Scale Out Core",
        "FlowTotalProgress": 0.38,
        "FlowTotalStatus": 1,
        "RequestId": "d9ad966c-9db0-409f-a2da-4c23350772d3",
        "StageDetails": [
            {
                "Desc": "已完成",
                "Endtime": "2024-10-29 20:24:41",
                "FailedReason": "",
                "HadWoodDetail": false,
                "IsShow": true,
                "IsSubFlow": false,
                "LanguageKey": "lookupResources",
                "Name": "Create Order",
                "Progress": 0,
                "Stage": "lookupResources",
                "Starttime": "2024-10-29 20:24:01",
                "Status": 2,
                "SubFlowFlag": "",
                "TimeConsuming": "takes 40s",
                "WoodJobId": 0
            },
            {
                "Desc": "已完成",
                "Endtime": "2024-10-29 20:24:43",
                "FailedReason": "",
                "HadWoodDetail": false,
                "IsShow": true,
                "IsSubFlow": false,
                "LanguageKey": "applyCvm",
                "Name": "Apply For Resource",
                "Progress": 0,
                "Stage": "applyCvm",
                "Starttime": "2024-10-29 20:24:41",
                "Status": 2,
                "SubFlowFlag": "",
                "TimeConsuming": "takes 2s",
                "WoodJobId": 0
            },
            {
                "Desc": "已完成",
                "Endtime": "2024-10-29 20:24:44",
                "FailedReason": "",
                "HadWoodDetail": false,
                "IsShow": true,
                "IsSubFlow": false,
                "LanguageKey": "bindTags",
                "Name": "Bind tag",
                "Progress": 0,
                "Stage": "bindTags",
                "Starttime": "2024-10-29 20:24:44",
                "Status": 2,
                "SubFlowFlag": "",
                "TimeConsuming": "takes 0s",
                "WoodJobId": 0
            },
            {
                "Desc": "未启动",
                "Endtime": "0000-00-00 00:00:00",
                "FailedReason": "",
                "HadWoodDetail": false,
                "IsShow": true,
                "IsSubFlow": false,
                "LanguageKey": "createSecurityGroup",
                "Name": "Initialize security group",
                "Progress": 0,
                "Stage": "createSecurityGroup",
                "Starttime": "0000-00-00 00:00:00",
                "Status": 4,
                "SubFlowFlag": "",
                "TimeConsuming": "",
                "WoodJobId": 0
            },
            {
                "Desc": "未启动",
                "Endtime": "0000-00-00 00:00:00",
                "FailedReason": "",
                "HadWoodDetail": false,
                "IsShow": true,
                "IsSubFlow": false,
                "LanguageKey": "addCVMAndCDBToWoodpecker",
                "Name": "Initialize resource",
                "Progress": 0,
                "Stage": "addCVMAndCDBToWoodpecker",
                "Starttime": "0000-00-00 00:00:00",
                "Status": 4,
                "SubFlowFlag": "",
                "TimeConsuming": "",
                "WoodJobId": 0
            },
            {
                "Desc": "未启动",
                "Endtime": "0000-00-00 00:00:00",
                "FailedReason": "",
                "HadWoodDetail": false,
                "IsShow": true,
                "IsSubFlow": false,
                "LanguageKey": "woodpeckerScaleoutCluster",
                "Name": "Prepare for scale-out",
                "Progress": 0,
                "Stage": "woodpeckerScaleoutCluster",
                "Starttime": "0000-00-00 00:00:00",
                "Status": 4,
                "SubFlowFlag": "",
                "TimeConsuming": "",
                "WoodJobId": 0
            },
            {
                "Desc": "未启动",
                "Endtime": "0000-00-00 00:00:00",
                "FailedReason": "",
                "HadWoodDetail": true,
                "IsShow": true,
                "IsSubFlow": true,
                "LanguageKey": "initializeService",
                "Name": "Initialize service",
                "Progress": 0,
                "Stage": "queryWoodpeckerFlow",
                "Starttime": "0000-00-00 00:00:00",
                "Status": 4,
                "SubFlowFlag": "",
                "TimeConsuming": "",
                "WoodJobId": 0
            },
            {
                "Desc": "未启动",
                "Endtime": "0000-00-00 00:00:00",
                "FailedReason": "",
                "HadWoodDetail": false,
                "IsShow": true,
                "IsSubFlow": false,
                "LanguageKey": "endPoint",
                "Name": "End task",
                "Progress": 0,
                "Stage": "endPoint",
                "Starttime": "0000-00-00 00:00:00",
                "Status": 4,
                "SubFlowFlag": "",
                "TimeConsuming": "",
                "WoodJobId": 0
            }
        ]
    }
}
```

