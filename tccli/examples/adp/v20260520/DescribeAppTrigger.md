**Example 1: 成功**



Input: 

```
tccli adp DescribeAppTrigger --cli-unfold-argument  \
    --AppId 2075415763781738240 \
    --TriggerId febb4930-0e2b-470b-9e24-04b73f9d773b \
    --UserId cuiyo******
```

Output: 
```
{
    "Response": {
        "Trigger": {
            "AppId": "2075415763781738240",
            "ExecuteConfig": {
                "WorkflowConfig": {
                    "ParamBindingsApi": {
                        "ParamList": []
                    },
                    "ParamBindingsWorkflow": {
                        "ParamList": [
                            {
                                "ParamName": "name",
                                "ParamType": 0,
                                "Value": {
                                    "VariableName": "Name"
                                }
                            }
                        ]
                    },
                    "WorkflowId": "2428abbd-9044-4031-8a5a-41ff3dc63fa2"
                }
            },
            "ExecuteType": 2,
            "FailedCount": "1",
            "PushConfig": {
                "PushChannel": 4,
                "PushTargetId": "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=446c1200-3738-4cdc-ac9e-01234578987",
                "PushTargetType": 2,
                "PushWebhookUrl": "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=446c1200-3738-4cdc-ac9e-01234578987"
            },
            "Status": 1,
            "SuccessCount": "0",
            "TriggerConfig": {
                "WebhookConfig": {
                    "ParamSchemaConfig": {
                        "SchemaList": [
                            {
                                "ParamName": "Name",
                                "ParamType": 0,
                                "Required": true,
                                "SubParamList": []
                            }
                        ]
                    },
                    "WebhookKey": "b4a451ee-a665-4f85-8a2e-4096af4ca342",
                    "WebhookToken": "2c95f3f3fa65d5c343f2e7a6bacfb9c7233ab6712a397ed5",
                    "WebhookUrl": "https://tde.xiaowei.cloud.tencent.com/adp/v2/app/2075415763781738240/trigger/webhook/b4a451ee-a665-4f85-8a2e-4096af4ca342"
                }
            },
            "TriggerId": "febb4930-0e2b-470b-9e24-04b73f9d773b",
            "TriggerName": "事件",
            "TriggerStatus": {
                "WebhookStatus": {
                    "WebhookUrl": "https://tde.xiaowei.cloud.tencent.com/adp/v2/app/2075415763781738240/trigger/webhook/b4a451ee-a665-4f85-8a2e-4096af4ca342"
                }
            },
            "TriggerType": 2
        },
        "RequestId": "8a92497b-4313-4cef-b91a-5ca5433d0dfd"
    }
}
```

