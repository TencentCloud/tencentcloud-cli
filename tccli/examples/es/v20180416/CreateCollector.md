**Example 1: 创建采集器**

根据输入参数创建采集器

Input: 

```
tccli es CreateCollector --cli-unfold-argument  \
    --CollectorType filebeat \
    --OutputInstance.InstanceId es-xxxxxxxx \
    --OutputInstance.Type elasticsearch \
    --CVMInstanceIds ins-xxxxxxxx \
    --CollectorConfigs.0.FileContent test \
    --CollectorConfigs.0.FileName filebeat.yml \
    --CollectorName test \
    --CollectorVersion 7.10.2
```

Output: 
```
{
    "Response": {
        "CollectorId": "coll-0xxxxxxx",
        "RequestId": "d7b76d5e-ad7d-4abd-b3b2-43b96dxxxxxx"
    }
}
```

