**Example 1: 查询日志**

查询指定告警策略的告警历史记录

Input: 

```
tccli cls GetAlarmLog --cli-unfold-argument  \
    --From 1702569600000 \
    --To 1702655999999 \
    --Query (alert_id:"alarm-5ce45495-09e8-4d58-8f36-768134bf330c") AND (monitored_object:"3c514e84-6f1f-46ec-afbf-05de6163f7fe") AND NOT condition_evaluate_result: "Skip" AND condition_evaluate_result:[* TO *] | SELECT count(*) as top50StatisticsTotalCount, count_if(condition_evaluate_result='ProcessError') as top50StatisticsFailureCount, count_if(notification_send_result!='NotSend') as top50NoticeTotalCount, count_if(notification_send_result='SendPartFail' or notification_send_result='SendFail') as top50NoticeFailureCount, alert_id, alert_name, monitored_object, topic_type, happen_threshold, alert_threshold, notify_template group by alert_id, alert_name, monitored_object,topic_type, happen_threshold, alert_threshold, notify_template order by top50StatisticsTotalCount desc limit 1 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "Analysis": true,
        "AnalysisRecords": [],
        "AnalysisResults": [
            {
                "Data": [
                    {
                        "Key": "topic_type",
                        "Value": "log"
                    },
                    {
                        "Key": "alert_threshold",
                        "Value": "15"
                    },
                    {
                        "Key": "top50NoticeFailureCount",
                        "Value": "0"
                    },
                    {
                        "Key": "happen_threshold",
                        "Value": "1"
                    },
                    {
                        "Key": "top50StatisticsFailureCount",
                        "Value": "0"
                    },
                    {
                        "Key": "alert_id",
                        "Value": "alarm-5ce45495-09e8-4d58-8f36-768134bf330c"
                    },
                    {
                        "Key": "top50StatisticsTotalCount",
                        "Value": "705"
                    },
                    {
                        "Key": "alert_name",
                        "Value": "EdgeOne 缓存命中率告警策略_100001127589"
                    },
                    {
                        "Key": "monitored_object",
                        "Value": "3c514e84-6f1f-46ec-afbf-05de6163f7fe"
                    },
                    {
                        "Key": "top50NoticeTotalCount",
                        "Value": "0"
                    },
                    {
                        "Key": "notify_template",
                        "Value": "notice-8e0660a4-197d-46b0-b1ef-e63571b7a438"
                    }
                ]
            }
        ],
        "ColNames": [
            "top50StatisticsTotalCount",
            "top50StatisticsFailureCount",
            "top50NoticeTotalCount",
            "top50NoticeFailureCount",
            "alert_id",
            "alert_name",
            "monitored_object",
            "topic_type",
            "happen_threshold",
            "alert_threshold",
            "notify_template"
        ],
        "Columns": [],
        "Context": "",
        "ListOver": true,
        "RequestId": "716f9f96-ed8c-4a20-9e75-dfa27ba9a273",
        "Results": []
    }
}
```

**Example 2: 查询指定告警策略和告警对象的告警历史记录**

查询指定告警策略和告警对象的告警历史记录

Input: 

```
tccli cls GetAlarmLog --cli-unfold-argument  \
    --From 1702569600000 \
    --To 1702655999999 \
    --Query alert_id:"alarm-5ce45495-09e8-4d58-8f36-768134bf330c" AND monitored_object:"3c514e84-6f1f-46ec-afbf-05de6163f7fe" \
    --Limit 1 \
    --Context 
```

Output: 
```
{
    "Response": {
        "Analysis": false,
        "AnalysisRecords": null,
        "AnalysisResults": [],
        "ColNames": [],
        "Columns": null,
        "Context": "Y29udGV4dC0yNmJkYjY1ZS1lODdjLTQ5Y2ItODdiYy0xNmUwNWFlYTYwM2MxNzAyNjEyMzA4MTU1",
        "ListOver": false,
        "RequestId": "aefbd480-35c5-43b7-b1df-d625727abebf",
        "Results": [
            {
                "FileName": "",
                "HostName": "",
                "IndexStatus": "",
                "LogJson": "{\"reach_trigger\":\"false\",\"label_string\":\"\",\"fire_time\":1702612278007,\"reach_notify\":\"false\",\"record_group_id\":\"\",\"topic_type\":\"log\",\"alert_threshold\":15,\"trigger_result\":\"success\",\"monitored_object\":\"3c514e84-6f1f-46ec-afbf-05de6163f7fe\",\"duration\":0,\"condition_evaluate_result\":\"QueryResultUnmatch\",\"notify_type\":2,\"summary_en\":\"The trigger condition is not met\",\"notification_send_result\":\"NotSend\",\"trigger_time\":1702612278,\"notify_template\":\"notice-8e0660a4-197d-46b0-b1ef-e63571b7a438\",\"summary_cn\":\"执行语句结果不满足触发条件\",\"alert_id\":\"alarm-5ce45495-09e8-4d58-8f36-768134bf330c\",\"notify_result\":\"success\",\"topic_name\":\"dyltest2\",\"process_result\":\"fail\",\"notify_failed_reason\":\"\",\"object_param\":\"[{\\\"EndTime\\\":1702612230000,\\\"StartTime\\\":1702608630000,\\\"TopicId\\\":\\\"3c514e84-6f1f-46ec-afbf-05de6163f7fe\\\",\\\"TopicName\\\":\\\"dyltest2\\\",\\\"TopicType\\\":\\\"log\\\",\\\"grammarVersion\\\":\\\"cql\\\"}]\",\"uin\":100001127589,\"topic_id\":\"3c514e84-6f1f-46ec-afbf-05de6163f7fe\",\"record_info\":\"\",\"notify_time\":1702612278,\"level\":\"Warn\",\"process_error_msg\":\"The conditions are not matched, no results\",\"trigger\":\"$1.hit_rate<50\",\"trigger_failed_reason\":\"The conditions are not matched, no results\",\"happen_threshold\":1,\"record_id\":\"9e35be9f-b617-4827-96c5-97a0383aad0f\",\"nick_name\":\"\",\"logset_id\":\"19b6cec0-b80f-4ffe-98de-239670e5b19d\",\"detail\":\"\",\"alert_name\":\"EdgeOne 缓存命中率告警策略_100001127589\",\"process_error_type\":\"QueryResultUnmatch\",\"status\":\"QueryResultUnmatch\"}",
                "PkgId": "",
                "PkgLogId": "",
                "RawLog": "",
                "Source": "",
                "Time": 1702612278007,
                "TopicId": "louder",
                "TopicName": "louder"
            }
        ]
    }
}
```

