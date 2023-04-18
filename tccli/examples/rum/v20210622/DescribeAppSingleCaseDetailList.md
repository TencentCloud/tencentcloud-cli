**Example 1: 查询 app 监控个例详情列表**



Input: 

```
tccli rum DescribeAppSingleCaseDetailList --cli-unfold-argument  \
    --Filter [] \
    --ProjectID 1 \
    --FilterSimple {"entrance_time__gte":1671025353000,"entrance_time__lte":1671284553000,"feature_md5":"8aba3b8538d7d843c558012c11219e1d","category__in":["PERF_CRASH"]} \
    --From singleton_v2_dist \
    --Fields [["as","device_id","device_id"],"entrance_time",["as","feature_md5","feature_md5"],["as","version","version"],["as","id","id"],["as","user_id","user_id"]] \
    --Limit 200 \
    --OrderBy 'entrance_time desc'
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

