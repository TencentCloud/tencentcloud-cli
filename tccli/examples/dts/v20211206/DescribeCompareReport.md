**Example 1: 查询一致性校验任务详情**



Input: 

```
tccli dts DescribeCompareReport --cli-unfold-argument  \
    --JobId dts-amm1jw5q \
    --CompareTaskId dts-amm1jw5q-cmp-bmuum7jk
```

Output: 
```
{
    "Response": {
        "Abstract": {
            "CheckedTables": 4,
            "Conclusion": "same",
            "DifferentRows": 0,
            "DifferentTables": 0,
            "SkippedTables": 0,
            "Status": "success",
            "TotalTables": 4
        },
        "Detail": {
            "Difference": {
                "Items": [],
                "TotalCount": 0
            },
            "Skipped": {
                "Items": [],
                "TotalCount": 0
            }
        },
        "RequestId": "ac300ff0-00f2-11ed-b005-4930e69d89c2"
    }
}
```

