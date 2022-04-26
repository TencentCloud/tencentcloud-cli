**Example 1: 修改数据加工任务**



Input: 

```
tccli cls ModifyDataTransform --cli-unfold-argument  \
    --DstResources.0.TopicId 81XXXXe5-e39e-4a1e-b2d4-a778df97d825 \
    --DstResources.0.Alias 别名 \
    --EnableFlag 0 \
    --EtlContent fields_set() \
    --Name 我的数据加工 \
    --TaskId e4fcXXXX-5e8a-4fe0-b52c-76eeca53e9af
```

Output: 
```
{
    "Response": {
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
    }
}
```

