**Example 1: 查询实例订阅指标**

查询实例订阅指标

Input: 

```
tccli tchousex DescribeMetricSubscription --cli-unfold-argument  \
    --InstanceId warehouse-j5bbsmrs \
    --ApiType QueryMetricSubscription \
    --MetricSubscriptionReq.Product cdwa \
    --MetricSubscriptionReq.Type impalad \
    --MetricSubscriptionReq.InstanceId warehouse-j5bbsmrs
```

Output: 
```
{
    "Response": {
        "ApiType": "QueryMetricSubscription",
        "ErrorMsg": "",
        "RequestId": "006ecd62-ff50-4591-95f8-2b42dbdd962f",
        "ReturnData": "[{\"ID\":648,\"CreateTime\":\"2024-11-21 19:18:34\",\"ModifyTime\":\"2024-11-21 19:18:34\",\"Product\":\"cdwa\",\"Type\":\"impalad\",\"Region\":\"ap-chongqing\",\"InstanceId\":\"warehouse-j5bbsmrs\",\"MetricName\":\"stream_load_per_second\"},{\"ID\":659,\"CreateTime\":\"2024-11-21 21:07:43\",\"ModifyTime\":\"2024-11-21 21:07:43\",\"Product\":\"cdwa\",\"Type\":\"impalad\",\"Region\":\"ap-chongqing\",\"InstanceId\":\"warehouse-j5bbsmrs\",\"MetricName\":\"files_merged_per_second\"},{\"ID\":660,\"CreateTime\":\"2024-11-21 21:07:47\",\"ModifyTime\":\"2024-11-21 21:07:47\",\"Product\":\"cdwa\",\"Type\":\"impalad\",\"Region\":\"ap-chongqing\",\"InstanceId\":\"warehouse-j5bbsmrs\",\"MetricName\":\"data_cache_hit_rate\"},{\"ID\":665,\"CreateTime\":\"2024-11-21 21:19:02\",\"ModifyTime\":\"2024-11-21 21:19:02\",\"Product\":\"cdwa\",\"Type\":\"impalad\",\"Region\":\"ap-chongqing\",\"InstanceId\":\"warehouse-j5bbsmrs\",\"MetricName\":\"cpu_load15\"},{\"ID\":670,\"CreateTime\":\"2024-11-21 21:19:17\",\"ModifyTime\":\"2024-11-21 21:19:17\",\"Product\":\"cdwa\",\"Type\":\"impalad\",\"Region\":\"ap-chongqing\",\"InstanceId\":\"warehouse-j5bbsmrs\",\"MetricName\":\"online_query_per_second\"},{\"ID\":1126,\"CreateTime\":\"2024-12-02 20:10:31\",\"ModifyTime\":\"2024-12-02 20:10:31\",\"Product\":\"cdwa\",\"Type\":\"impalad\",\"Region\":\"ap-chongqing\",\"InstanceId\":\"warehouse-j5bbsmrs\",\"MetricName\":\"is_up\"},{\"ID\":1127,\"CreateTime\":\"2024-12-02 20:10:31\",\"ModifyTime\":\"2024-12-02 20:10:31\",\"Product\":\"cdwa\",\"Type\":\"impalad\",\"Region\":\"ap-chongqing\",\"InstanceId\":\"warehouse-j5bbsmrs\",\"MetricName\":\"cpu_use_rate\"},{\"ID\":1128,\"CreateTime\":\"2024-12-02 20:10:31\",\"ModifyTime\":\"2024-12-02 20:10:31\",\"Product\":\"cdwa\",\"Type\":\"impalad\",\"Region\":\"ap-chongqing\",\"InstanceId\":\"warehouse-j5bbsmrs\",\"MetricName\":\"cpu_load1\"},{\"ID\":1129,\"CreateTime\":\"2024-12-02 20:10:31\",\"ModifyTime\":\"2024-12-02 20:10:31\",\"Product\":\"cdwa\",\"Type\":\"impalad\",\"Region\":\"ap-chongqing\",\"InstanceId\":\"warehouse-j5bbsmrs\",\"MetricName\":\"mem_use_rate\"},{\"ID\":1130,\"CreateTime\":\"2024-12-02 20:10:31\",\"ModifyTime\":\"2024-12-02 20:10:31\",\"Product\":\"cdwa\",\"Type\":\"impalad\",\"Region\":\"ap-chongqing\",\"InstanceId\":\"warehouse-j5bbsmrs\",\"MetricName\":\"online_sql_running\"},{\"ID\":1131,\"CreateTime\":\"2024-12-02 20:10:31\",\"ModifyTime\":\"2024-12-02 20:10:31\",\"Product\":\"cdwa\",\"Type\":\"impalad\",\"Region\":\"ap-chongqing\",\"InstanceId\":\"warehouse-j5bbsmrs\",\"MetricName\":\"stream_load_running\"}]"
    }
}
```

