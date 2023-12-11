**Example 1: 创建日志采集规则**

创建采集规则是调用

Input: 

```
tccli tke CreateCLSLogConfig --cli-unfold-argument  \
    --LogConfig {\"apiVersion\":\"cls.cloud.tencent.com/v1\",\"kind\":\"LogConfig\",\"metadata\":{\"name\":\"stdout\"},\"spec\":{\"clsDetail\":{\"logType\":\"minimalist_log\",\"logFormat\":\"default\",\"topicId\":null,\"userDefineRule\":null,\"extractRule\":{\"timeKey\":null,\"timeFormat\":null,\"delimiter\":null,\"logRegex\":null,\"beginningRegex\":null,\"keys\":[],\"filterKeys\":[],\"filterRegex\":[],\"unMatchUpload\":\"false\",\"unMatchedKey\":null,\"backtracking\":\"0\"},\"topicName\":null,\"indexs\":[],\"region\":null},\"inputDetail\":{\"type\":\"container_stdout\",\"containerStdout\":{\"allContainers\":false,\"namespace\":null,\"workloads\":[{\"namespace\":\"default\",\"kind\":\"deployment\",\"name\":\"stdout\",\"container\":\"\"}],\"includeLabels\":null,\"container\":null,\"metadataLabels\":[]},\"containerFile\":null,\"hostFile\":null},\"kafkaDetail\":null}} \
    --ClusterId cls-kaftesta
```

Output: 
```
{
    "Response": {
        "RequestId": "f12a6e20-f950-4af9-8f8b-b6329a4961c2"
    }
}
```

