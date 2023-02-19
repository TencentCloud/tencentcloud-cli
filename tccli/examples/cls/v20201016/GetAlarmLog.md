**Example 1: 查询日志**

查询指定告警策略的告警历史记录

Input: 

```
tccli cls GetAlarmLog --cli-unfold-argument  \
    --From 1676615510870 \
    --To 1676619110870 \
    --Query alert_id: alarm-3e6131b1-689a-xxxx-8e2d-62ba80e6d91e \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "Context": "Y29udGV4dC03MTI5NGYwZS1kY2IyLTQ0MTktYmQyMy01ZDgwNTcyN2Y0OTExNjc2NjE5Mzk5Mjg3",
        "ListOver": false,
        "Analysis": false,
        "ColNames": [],
        "Columns": null,
        "Results": [
            {
                "Time": 1676618994000,
                "TopicId": "louder",
                "TopicName": "louder",
                "Source": "",
                "FileName": "",
                "HostName": "",
                "PkgId": "",
                "PkgLogId": "",
                "LogJson": "{\"reach_trigger\":\"true\",\"notify_time\":1676618994,\"reach_notify\":\"false\",\"process_error_msg\":\"AlertThreshold Unreached\",\"record_group_id\":\"\",\"trigger\":\"$1.Warning事件数 > 0\",\"trigger_failed_reason\":\"matched\",\"alert_threshold\":15,\"trigger_result\":\"success\",\"monitored_object\":\"993bba4d-9494-4023-xxxx-f06c1b8c2983\",\"happen_threshold\":1,\"notify_type\":1,\"record_id\":\"\",\"trigger_time\":1676618994,\"notify_template\":\"notice-a1d2a4a6-c731-4386-869a-5ba91b1bb26c\",\"alert_id\":\"alarm-3e6131b1-689a-xxxx-8e2d-62ba80e6d91e\",\"notify_result\":\"fail\",\"process_result\":\"fail\",\"notify_failed_reason\":\"AlertThreshold Unreached\",\"uin\":10000100xxxx,\"topic_id\":\"993bba4d-9494-4023-xxxx-f06c1b8c2983\",\"record_info\":\"\",\"alert_name\":\"TKE Demo事件日志告警策略_10000100xxxx\",\"process_error_type\":\"UnreachedThreshold\"}"
            }
        ],
        "AnalysisResults": [],
        "AnalysisRecords": null,
        "RequestId": "53fa03fb-a0f6-4ac0-afe8-de697b586eb0"
    }
}
```

