**Example 1: 查询dspm数据识别数据项列表**



Input: 

```
tccli csip DescribeDspmIdentifyRuleList --cli-unfold-argument  \
    --Filter.Filters.0.Name Scope \
    --Filter.Filters.0.Values 1
```

Output: 
```
{
    "Response": {
        "DataSet": [
            {
                "Description": "",
                "Id": 10006,
                "Name": "kyrie-kv-rule-001",
                "Status": 1,
                "StructuredStatus": true,
                "Type": 1,
                "UnStructuredStatus": false,
                "UpdateTime": "2026-05-27 18:04:57"
            }
        ],
        "TotalCount": 136,
        "RequestId": "8cc2afe2-d1fe-4cf6-92b6-bea279c710ef"
    }
}
```

