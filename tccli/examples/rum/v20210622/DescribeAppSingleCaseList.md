**Example 1: 查询 app 个例聚合列表**



Input: 

```
tccli rum DescribeAppSingleCaseList --cli-unfold-argument  \
    --Filter [] \
    --ProjectID 1 \
    --FilterSimple {"entrance_time__gte":1671370185000,"entrance_time__lte":1671456585000,"category__in":["PERF_CRASH"]} \
    --From 'singleton_v2_dist' \
    --Fields ["app_id",["as",["any",["cast","feature","'String'"]],"row_feature"],["as",["max","entrance_time"],"last_entrance_time"],"feature_md5",["as",["uniq","device_id"],"crash_user_cnt"],["as",["count",1],"crash_cnt"],["as",["aggByPartition","sum","crash_user_cnt","app_id"],"total_crash_user_cnt"],["as",["aggByPartition","sum","crash_cnt","app_id"],"total_crash_cnt"]] \
    --GroupBy feature_md5 app_id platform \
    --OrderBy 'crash_cnt desc'
```

Output: 
```
{
    "Response": {
        "Data": "'{\"status\":\"ok\",\"code\":10000,\"msg\":\"ok\",\"data\":[]}'",
        "RequestId": "a2bcd13d-000f-4b84-a72e-6d4229079014"
    }
}
```

