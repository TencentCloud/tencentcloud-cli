**Example 1: 成功**



Input: 

```
tccli adp CreateAppTrigger --cli-unfold-argument  \
    --AppId 20754157*********** \
    --ExecuteConfig.WorkflowConfig.ParamBindingsWorkflow.ParamList.0.ParamName name \
    --ExecuteConfig.WorkflowConfig.ParamBindingsWorkflow.ParamList.0.ParamType 0 \
    --ExecuteConfig.WorkflowConfig.ParamBindingsWorkflow.ParamList.0.Value.VariableName Name \
    --ExecuteConfig.WorkflowConfig.WorkflowId 2428abbd-9044-4031-8a5a-41ff3dc63fa2 \
    --ExecuteType 2 \
    --PushConfig.PushChannel 4 \
    --PushConfig.PushTargetId https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=*********************************** \
    --PushConfig.PushTargetType 2 \
    --PushConfig.PushWebhookUrl https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=*********************************** \
    --TriggerConfig.WebhookConfig.ParamSchemaConfig.SchemaList.0.ParamName Name \
    --TriggerConfig.WebhookConfig.ParamSchemaConfig.SchemaList.0.ParamType 0 \
    --TriggerConfig.WebhookConfig.ParamSchemaConfig.SchemaList.0.Required True \
    --TriggerConfig.WebhookConfig.WebhookKey ************************************ \
    --TriggerConfig.WebhookConfig.WebhookToken ************************************************ \
    --TriggerConfig.WebhookConfig.WebhookUrl https:/adp.cloud.tencent.com/adp/v2/app/2075415763781738240/trigger/webhook/************************************ \
    --TriggerName 事件 \
    --TriggerType 2
```

Output: 
```
{
    "Response": {
        "TriggerId": "a0129199-5942-478b-af9f-16b201295e65",
        "RequestId": "03c7e279-063b-4900-a6f3-df82f5bc0bd4"
    }
}
```

