**Example 1: 通过yaml文件创建指标预聚合任务**

通过yaml文件创建指标预聚合任务

Input: 

```
tccli cls CreateRecordingRuleYamlTask --cli-unfold-argument  \
    --TopicId e66648c8-0d90-4a32-8009-b4ee9f4b3c7c \
    --YamlConfigName demo \
    --EnableFlag 1 \
    --HasServicesLog 2 \
    --ProcessPeriod 1 \
    --ProcessDelay 30 \
    --YamlContent groups:
  - name: example
    rules:
    - record: code:prometheus_http_requests_total:sum
      expr: sum by (code) (prometheus_http_requests_total) \
    --DstTopicId e66648c8-0d90-4a32-8009-b4ee9f4b3c7c \
    --ProcessStartTime 1778309756421
```

Output: 
```
{
    "Response": {
        "YamlId": "abdcebec-0242-43af-bb20-270359fb54a7",
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
    }
}
```

