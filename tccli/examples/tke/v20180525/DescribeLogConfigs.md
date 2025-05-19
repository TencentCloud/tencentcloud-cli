**Example 1: 查询采集规则**

查询采集规则

Input: 

```
tccli tke DescribeLogConfigs --cli-unfold-argument  \
    --ClusterId cls-bz7ge4wl
```

Output: 
```
{
    "Response": {
        "RequestId": "583e6c4b-ff24-42f8-87f1-37e4c00d81b7",
        "Total": 1,
        "LogConfigs": "{\"ItemCount\":1,\"Items\":[{\"apiVersion\":\"cls.cloud.tencent.com/v1\",\"kind\":\"LogConfig\",\"metadata\":{\"name\":\"test1\"},\"spec\":{\"clsDetail\":{\"extractRule\":{\"backtracking\":\"0\",\"isGBK\":\"false\",\"jsonStandard\":\"false\",\"unMatchUpload\":\"false\"},\"indexs\":[{\"indexName\":\"namespace\"},{\"indexName\":\"pod_name\"},{\"indexName\":\"container_name\"}],\"logFormat\":\"default\",\"logType\":\"minimalist_log\",\"maxSplitPartitions\":0,\"period\":30,\"region\":\"ap-chengdu\",\"storageType\":\"\",\"topicId\":\"2912eb16-a56c-4b9b-adb0-9828db1ad342\"},\"inputDetail\":{\"containerStdout\":{\"containerOperator\":\"in\",\"includeLabels\":{\"app\":\"test1\"},\"metadataContainer\":[\"namespace\",\"pod_name\",\"pod_ip\",\"pod_uid\",\"container_id\",\"container_name\",\"image_name\",\"cluster_id\"],\"namespace\":\"default\",\"nsLabelSelector\":\"\"},\"type\":\"container_stdout\"},\"kafkaDetail\":{\"brokers\":\"\",\"instanceId\":\"\",\"kafkaType\":\"\",\"logType\":\"\",\"messageKey\":{\"value\":\"\",\"valueFrom\":{\"fieldRef\":{\"fieldPath\":\"\"}}},\"metadata\":{},\"timestampFormat\":\"\",\"timestampKey\":\"\",\"topic\":\"\"}},\"status\":{\"code\":\"success\",\"reason\":\"success\",\"status\":\"Synced\"}}]}"
    }
}
```

