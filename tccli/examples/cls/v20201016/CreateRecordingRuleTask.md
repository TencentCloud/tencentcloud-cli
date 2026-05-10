**Example 1: 创建指标预聚合任务**

创建指标预聚合任务

Input: 

```
tccli cls CreateRecordingRuleTask --cli-unfold-argument  \
    --TopicId e66648c8-0d90-xxxx-8009-b4ee9f4b3c7c \
    --Name demo \
    --EnableFlag 1 \
    --RecordingRuleContent sum by (code)(prometheus_http_requests_total) \
    --MetricName demo_metric \
    --CustomMetricLabels.0.Key demo_key \
    --CustomMetricLabels.0.Value demo_value \
    --HasServicesLog 2 \
    --ProcessPeriod 1 \
    --ProcessDelay 30 \
    --DstTopicId e66648c8-0d90-xxxx-8009-b4ee9f4b3c7c \
    --ProcessStartTime 1778308263665
```

Output: 
```
{
    "Response": {
        "TaskId": "abdcebec-0242-43af-bb20-270359fb54a7",
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
    }
}
```

