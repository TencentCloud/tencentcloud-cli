**Example 1: 仅终止等待中的实例**

OnlyKillPendingRuns=true 时仅终止等待资源中的实例，运行中的不受影响

Input: 

```
tccli databuddy KillWorkflowRun --cli-unfold-argument  \
    --WorkspaceId 17623497097012366 \
    --WorkflowId 8e116990-d2b2-451a-84d3-2f890b38de4f \
    --WorkflowRunIds 8e116990-d2b2-451a-84d3-2f890b38de4f_1790157828891 \
    --OnlyKillPendingRuns True
```

Output: 
```
{
    "Response": {
        "Data": {
            "ActionResults": [
                {
                    "ErrorMessage": "",
                    "OpStatus": true,
                    "RunActionId": "cmd_20260923180358_000001",
                    "WorkflowId": "8e116990-d2b2-451a-84d3-2f890b38de4f",
                    "WorkflowName": "",
                    "WorkflowRunId": "8e116990-d2b2-451a-84d3-2f890b38de4f_1790157828891"
                }
            ]
        },
        "RequestId": "d8344b33-2948-4a51-949a-aa7f22039440"
    }
}
```

**Example 2: 终止工作流的运行**



Input: 

```
tccli databuddy KillWorkflowRun --cli-unfold-argument  \
    --WorkspaceId 17697410068842890 \
    --WorkflowId 8e0e3485-2736-4530-92ed-932e019898f1 \
    --WorkflowRunIds 8e0e3485-2736-4530-92ed-932e019898f1_1786115878097
```

Output: 
```
{
    "Response": {
        "Data": {
            "ActionResults": [
                {
                    "ErrorMessage": "",
                    "OpStatus": true,
                    "RunActionId": "cmd_20260807235246_000001",
                    "WorkflowId": "8e0e3485-2736-4530-92ed-932e019898f1_1786115878097",
                    "WorkflowName": "",
                    "WorkflowRunId": ""
                }
            ]
        },
        "RequestId": "43957900-50db-43be-9cb2-9af3b1f278c0"
    }
}
```

**Example 3: 终止所有运行中的实例**

KillAllRuns=true 时终止该工作流全部运行中实例

Input: 

```
tccli databuddy KillWorkflowRun --cli-unfold-argument  \
    --WorkspaceId 17623497097012366 \
    --WorkflowId 8e116990-d2b2-451a-84d3-2f890b38de4f \
    --KillAllRuns True
```

Output: 
```
{
    "Response": {
        "Data": {
            "ActionResults": [
                {
                    "ErrorMessage": "",
                    "OpStatus": true,
                    "RunActionId": "cmd_20260923172209_000001",
                    "WorkflowId": "8e116990-d2b2-451a-84d3-2f890b38de4f",
                    "WorkflowName": "",
                    "WorkflowRunId": "8e116990-d2b2-451a-84d3-2f890b38de4f_1790155291965"
                }
            ]
        },
        "RequestId": "c227081f-3a22-43e7-8ca6-557cc006efbc"
    }
}
```

