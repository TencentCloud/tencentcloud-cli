**Example 1: 弹性集群创建日志采集规则**

弹性集群创建日志采集规则时调用

Input: 

```
tccli tke CreateEksLogConfig --cli-unfold-argument  \
    --LogConfig {\"apiVersion\":\"cls.cloud.tencent.com/v1\",\"kind\":\"LogConfig\",\"metadata\":{\"name\":\"stdout\"},\"spec\":{\"clsDetail\":{\"logType\":\"minimalist_log\",\"logFormat\":\"default\",\"topicId\":null,\"userDefineRule\":null,\"extractRule\":{\"timeKey\":null,\"timeFormat\":null,\"delimiter\":null,\"logRegex\":null,\"beginningRegex\":null,\"keys\":[],\"filterKeys\":[],\"filterRegex\":[],\"unMatchUpload\":\"false\",\"unMatchedKey\":null,\"backtracking\":\"0\"},\"topicName\":null,\"indexs\":[],\"region\":null},\"inputDetail\":{\"type\":\"container_stdout\",\"containerStdout\":{\"allContainers\":false,\"namespace\":null,\"workloads\":[{\"namespace\":\"default\",\"kind\":\"deployment\",\"name\":\"stdout\",\"container\":\"\"}],\"includeLabels\":null,\"container\":null,\"metadataLabels\":[]},\"containerFile\":null,\"hostFile\":null},\"kafkaDetail\":null}} \
    --ClusterId cls-kaftesta \
    --LogsetId tas89a94-d952-410a-a393-9224de64test
```

Output: 
```
{
    "Response": {
        "TopicId": "b54181b9-422e-4a6b-8ce1-30d64ddcb02b",
        "RequestId": "f12a6e20-f950-4af9-8f8b-b6329a4961c2"
    }
}
```

