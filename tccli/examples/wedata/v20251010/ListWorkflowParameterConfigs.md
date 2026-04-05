**Example 1: 成功**

查询系统工作流内置参数成功

Input: 

```
tccli wedata ListWorkflowParameterConfigs --cli-unfold-argument  \
    --Type WORKFLOW
```

Output: 
```
{
    "Response": {
        "Data": {
            "ParamList": [
                {
                    "WorkflowParameterConfigDesc": "工作流Id",
                    "WorkflowParameterConfigId": 1,
                    "WorkflowParameterConfigKey": "workflow.id",
                    "WorkflowParameterConfigType": "WORKFLOW"
                },
                {
                    "WorkflowParameterConfigDesc": "NULL",
                    "WorkflowParameterConfigId": 2,
                    "WorkflowParameterConfigKey": "workflow.name",
                    "WorkflowParameterConfigType": "WORKFLOW"
                },
                {
                    "WorkflowParameterConfigDesc": "NULL",
                    "WorkflowParameterConfigId": 3,
                    "WorkflowParameterConfigKey": "workflow.repair_count",
                    "WorkflowParameterConfigType": "WORKFLOW"
                },
                {
                    "WorkflowParameterConfigDesc": "NULL",
                    "WorkflowParameterConfigId": 4,
                    "WorkflowParameterConfigKey": "workflow.run_id",
                    "WorkflowParameterConfigType": "WORKFLOW"
                },
                {
                    "WorkflowParameterConfigDesc": "NULL",
                    "WorkflowParameterConfigId": 5,
                    "WorkflowParameterConfigKey": "workflow.start_time.year",
                    "WorkflowParameterConfigType": "WORKFLOW"
                },
                {
                    "WorkflowParameterConfigDesc": "NULL",
                    "WorkflowParameterConfigId": 6,
                    "WorkflowParameterConfigKey": "workflow.start_time.month",
                    "WorkflowParameterConfigType": "WORKFLOW"
                },
                {
                    "WorkflowParameterConfigDesc": "",
                    "WorkflowParameterConfigId": 7,
                    "WorkflowParameterConfigKey": "workflow.start_time.day",
                    "WorkflowParameterConfigType": "WORKFLOW"
                },
                {
                    "WorkflowParameterConfigDesc": "",
                    "WorkflowParameterConfigId": 8,
                    "WorkflowParameterConfigKey": "workflow.start_time.hour",
                    "WorkflowParameterConfigType": "WORKFLOW"
                },
                {
                    "WorkflowParameterConfigDesc": "",
                    "WorkflowParameterConfigId": 9,
                    "WorkflowParameterConfigKey": "workflow.start_time.minute",
                    "WorkflowParameterConfigType": "WORKFLOW"
                },
                {
                    "WorkflowParameterConfigDesc": "",
                    "WorkflowParameterConfigId": 10,
                    "WorkflowParameterConfigKey": "workflow.start_time.second",
                    "WorkflowParameterConfigType": "WORKFLOW"
                },
                {
                    "WorkflowParameterConfigDesc": "",
                    "WorkflowParameterConfigId": 11,
                    "WorkflowParameterConfigKey": "workflow.start_time.is_weekday",
                    "WorkflowParameterConfigType": "WORKFLOW"
                },
                {
                    "WorkflowParameterConfigDesc": "",
                    "WorkflowParameterConfigId": 12,
                    "WorkflowParameterConfigKey": "workflow.start_time.iso_date",
                    "WorkflowParameterConfigType": "WORKFLOW"
                },
                {
                    "WorkflowParameterConfigDesc": "",
                    "WorkflowParameterConfigId": 13,
                    "WorkflowParameterConfigKey": "workflow.start_time.iso_datetime",
                    "WorkflowParameterConfigType": "WORKFLOW"
                },
                {
                    "WorkflowParameterConfigDesc": "",
                    "WorkflowParameterConfigId": 14,
                    "WorkflowParameterConfigKey": "workflow.start_time.iso_weekday",
                    "WorkflowParameterConfigType": "WORKFLOW"
                },
                {
                    "WorkflowParameterConfigDesc": "",
                    "WorkflowParameterConfigId": 15,
                    "WorkflowParameterConfigKey": "workflow.start_time.timestamp_ms",
                    "WorkflowParameterConfigType": "WORKFLOW"
                },
                {
                    "WorkflowParameterConfigDesc": "",
                    "WorkflowParameterConfigId": 16,
                    "WorkflowParameterConfigKey": "workflow.trigger.time.year",
                    "WorkflowParameterConfigType": "WORKFLOW"
                },
                {
                    "WorkflowParameterConfigDesc": "",
                    "WorkflowParameterConfigId": 17,
                    "WorkflowParameterConfigKey": "workflow.trigger.time.month",
                    "WorkflowParameterConfigType": "WORKFLOW"
                },
                {
                    "WorkflowParameterConfigDesc": "",
                    "WorkflowParameterConfigId": 18,
                    "WorkflowParameterConfigKey": "workflow.trigger.time.day",
                    "WorkflowParameterConfigType": "WORKFLOW"
                },
                {
                    "WorkflowParameterConfigDesc": "",
                    "WorkflowParameterConfigId": 19,
                    "WorkflowParameterConfigKey": "workflow.trigger.time.hour",
                    "WorkflowParameterConfigType": "WORKFLOW"
                },
                {
                    "WorkflowParameterConfigDesc": "",
                    "WorkflowParameterConfigId": 20,
                    "WorkflowParameterConfigKey": "workflow.trigger.time.minute",
                    "WorkflowParameterConfigType": "WORKFLOW"
                },
                {
                    "WorkflowParameterConfigDesc": "",
                    "WorkflowParameterConfigId": 21,
                    "WorkflowParameterConfigKey": "workflow.trigger.time.second",
                    "WorkflowParameterConfigType": "WORKFLOW"
                },
                {
                    "WorkflowParameterConfigDesc": "",
                    "WorkflowParameterConfigId": 22,
                    "WorkflowParameterConfigKey": "workflow.start_time.is_weekday",
                    "WorkflowParameterConfigType": "WORKFLOW"
                },
                {
                    "WorkflowParameterConfigDesc": "",
                    "WorkflowParameterConfigId": 23,
                    "WorkflowParameterConfigKey": "workflow.trigger.time.iso_date",
                    "WorkflowParameterConfigType": "WORKFLOW"
                },
                {
                    "WorkflowParameterConfigDesc": "",
                    "WorkflowParameterConfigId": 24,
                    "WorkflowParameterConfigKey": "workflow.trigger.time.iso_datetime",
                    "WorkflowParameterConfigType": "WORKFLOW"
                },
                {
                    "WorkflowParameterConfigDesc": "",
                    "WorkflowParameterConfigId": 25,
                    "WorkflowParameterConfigKey": "workflow.trigger.time.iso_weekday",
                    "WorkflowParameterConfigType": "WORKFLOW"
                },
                {
                    "WorkflowParameterConfigDesc": "",
                    "WorkflowParameterConfigId": 26,
                    "WorkflowParameterConfigKey": "workflow.trigger.time.timestamp_ms",
                    "WorkflowParameterConfigType": "WORKFLOW"
                },
                {
                    "WorkflowParameterConfigDesc": "",
                    "WorkflowParameterConfigId": 27,
                    "WorkflowParameterConfigKey": "workspace.id",
                    "WorkflowParameterConfigType": "WORKFLOW"
                },
                {
                    "WorkflowParameterConfigDesc": "",
                    "WorkflowParameterConfigId": 28,
                    "WorkflowParameterConfigKey": "workspace.url",
                    "WorkflowParameterConfigType": "WORKFLOW"
                }
            ]
        },
        "RequestId": "d5dcf8e2-1281-4930-b644-35c6fc968dc9"
    }
}
```

