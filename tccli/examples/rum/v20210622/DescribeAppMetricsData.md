**Example 1: 查询 app 指标数据**



Input: 

```
tccli rum DescribeAppMetricsData --cli-unfold-argument  \
    --Filter '[\"or\",[\"and\",[\"equals\",\"category\",\"'PERF_CRASH'\"],[\"in\",\"d4\",[\"array\",\"'Java'\",\"'Native'\",\"'normal_crash'\",\"'no_crash'\",\"'deadlock'\",\"'foom'\"]],[\"in\",\"sd1\",[\"array\",\"'v1'\",\"'v2'\"]]],[\"and\",[\"equals\",\"category\",\"'APP_LAUNCH'\"],[\"greaterOrEquals\",\"sdk_ver\",\"'5.2.1'\"]],[\"and\",[\"equals\",\"category\",\"'PERF_MASTER_TOKEN_FLOW'\"],[\"less\",\"sdk_ver\",\"'5.2.1'\"]],[\"and\",[\"equals\",\"category\",\"'PERF_MASTER_TOKEN_FLOW'\"],[\"equals\",\"sdk_ver\",\"'unknown'\"]]]' \
    --ProjectID 1 \
    --FilterSimple {"category__in":["PERF_CRASH","APP_LAUNCH","PERF_MASTER_TOKEN_FLOW"],"entrance_time__gte":"1670939782000","entrance_time__lte":"1671026182000"} \
    --From 'kv_7_dist' \
    --Fields '[[\"as\",[\"if\",[\"equals\",\"launch_cnt\",[\"toInt64\",0]],0,[\"div\",\"crash_cnt\",\"launch_cnt\"]],\"crash_rate\"],[\"as\",[\"countIf\",[\"and\",[\"equals\",\"category\",\"'PERF_CRASH'\"],[\"notEquals\",\"d4\",\"'no_crash'\"]]],\"crash_cnt\"],[\"as\",[\"if\",[\"equals\",\"launch_cnt\",[\"toInt64\",0]],0,[\"div\",\"crash_user_cnt\",\"user_cnt\"]],\"crash_user_rate\"],[\"as\",[\"uniq\",[\"if\",[\"and\",[\"equals\",\"category\",\"'PERF_CRASH'\"],[\"notEquals\",\"d4\",\"'no_crash'\"]],\"device_id\",\"null\"]],\"crash_user_cnt\"],[\"as\",[\"uniq\",[\"if\",[\"or\",[\"and\",[\"equals\",\"category\",\"'APP_LAUNCH'\"],[\"greaterOrEquals\",\"sdk_ver\",\"'5.2.1'\"]],[\"and\",[\"equals\",\"category\",\"'PERF_MASTER_TOKEN_FLOW'\"],[\"less\",\"sdk_ver\",\"'5.2.1'\"]],[\"and\",[\"equals\",\"d4\",\"'no_crash'\"],[\"less\",\"sdk_ver\",\"'5.2.1'\"]],[\"and\",[\"equals\",\"category\",\"'PERF_MASTER_TOKEN_FLOW'\"],[\"equals\",\"sdk_ver\",\"'unknown'\"]],[\"and\",[\"equals\",\"d4\",\"'no_crash'\"],[\"equals\",\"sdk_ver\",\"'unknown'\"]]],\"device_id\",\"null\"]],\"user_cnt\"],[\"as\",[\"countIf\",[\"or\",[\"and\",[\"equals\",\"category\",\"'APP_LAUNCH'\"],[\"greaterOrEquals\",\"sdk_ver\",\"'5.2.1'\"]],[\"and\",[\"equals\",\"category\",\"'PERF_MASTER_TOKEN_FLOW'\"],[\"less\",\"sdk_ver\",\"'5.2.1'\"]],[\"and\",[\"equals\",\"d4\",\"'no_crash'\"],[\"less\",\"sdk_ver\",\"'5.2.1'\"]],[\"and\",[\"equals\",\"category\",\"'PERF_MASTER_TOKEN_FLOW'\"],[\"equals\",\"sdk_ver\",\"'unknown'\"]],[\"and\",[\"equals\",\"d4\",\"'no_crash'\"],[\"equals\",\"sdk_ver\",\"'unknown'\"]]]],\"launch_cnt\"],[\"as\",\"launch_cnt\",\"total_cnt\"]]'
```

Output: 
```
{
    "Response": {
        "Data": "{\n    \"status\": \"ok\",\n    \"code\": 10000,\n    \"msg\": \"ok\",\n    \"data\": [\n        {\n            \"crash_cnt\": 18782,\n            \"crash_rate\": 0.7724132258595163,\n            \"crash_user_cnt\": 1,\n            \"crash_user_rate\": 1,\n            \"launch_cnt\": 24316,\n            \"total_cnt\": 24316,\n            \"user_cnt\": 1\n        }\n    ]\n}",
        "RequestId": "77b45639-2b70-40b5-b9af-739488787109"
    }
}
```

