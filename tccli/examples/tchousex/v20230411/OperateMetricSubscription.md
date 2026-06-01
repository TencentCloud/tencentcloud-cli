**Example 1: 实例关注指标**

实例关注指标

Input: 

```
tccli tchousex OperateMetricSubscription --cli-unfold-argument  \
    --InstanceId warehouse-l1pqs6lp \
    --ApiType SaveMetricSubscription \
    --MetricSubscriptionReq.Product cdwa \
    --MetricSubscriptionReq.Type impalad \
    --MetricSubscriptionReq.InstanceId warehouse-l1pqs6lp \
    --MetricSubscriptionReq.MetricName is_up
```

Output: 
```
{
    "Response": {
        "ApiType": "SaveMetricSubscription",
        "ErrorMsg": "SaveMetricSubscription duplicate, metricSubscription : &{0 2024-12-03 14:25:54 2024-12-03 14:25:54 cdwa impalad ap-chongqing warehouse-l1pqs6lp is_up}",
        "ExtFullSubscriptionData": "",
        "RequestId": "8a5b248c-147d-4679-977b-15101743e570",
        "ReturnData": "{\"ID\":0,\"CreateTime\":\"2024-12-03 14:25:54\",\"ModifyTime\":\"2024-12-03 14:25:54\",\"Product\":\"cdwa\",\"Type\":\"impalad\",\"Region\":\"ap-chongqing\",\"InstanceId\":\"warehouse-l1pqs6lp\",\"MetricName\":\"is_up\"}"
    }
}
```

