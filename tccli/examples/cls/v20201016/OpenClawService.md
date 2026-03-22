**Example 1: 创建OpenClawService日志服务**



Input: 

```
tccli cls OpenClawService --cli-unfold-argument  \
    --Tag ClawPro
```

Output: 
```
{
    "Response": {
        "AppLogConfigId": "b1ba2eba-8d9f-4091-a6a8-820ac2b2d85c",
        "AppLogConfigName": "clawpro_app_log_collect",
        "LogsetId": "claw-logset-ap-guangzhou-open-1254139626",
        "LogsetName": "claw_logset",
        "MachineGroupId": "da7b700c-2d4b-475b-b8a1-d2ecfbe3df81",
        "MachineGroupName": "ClawPro_MachineGroup",
        "MetricTopicId": "clawpro-metric-topic-ap-guangzhou-open-1254139626",
        "MetricTopicName": "clawpro_metric_topic",
        "SessionLogConfigId": "39134e29-ed4d-4299-9929-2fa94a060838",
        "SessionLogConfigName": "clawpro_session_log_collect",
        "TopicId": "clawpro-topic-ap-guangzhou-open-1254139626",
        "TopicName": "clawpro_log_topic",
        "RequestId": "ca5966ab-6fa6-4cdb-bdf7-695b551c005b"
    }
}
```

