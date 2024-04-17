**Example 1: 查询质量评分**

查询质量评分

Input: 

```
tccli wedata DescribeQualityScore --cli-unfold-argument  \
    --StatisticsDate 1647878400 \
    --ProjectId 1 \
    --DatasourceId 232
```

Output: 
```
{
    "Response": {
        "Data": {
            "CompositeScore": 13.64,
            "ScoringDistribution": [
                {
                    "Level": 1,
                    "Scale": 0,
                    "TableNumber": 0
                },
                {
                    "Level": 2,
                    "Scale": 0,
                    "TableNumber": 0
                },
                {
                    "Level": 3,
                    "Scale": 0,
                    "TableNumber": 0
                },
                {
                    "Level": 4,
                    "Scale": 0,
                    "TableNumber": 0
                },
                {
                    "Level": 5,
                    "Scale": 100,
                    "TableNumber": 1
                }
            ],
            "TotalTableNumber": 1
        },
        "RequestId": "2085cb56-c8ef-42d6-8e3a-5854aa3ce46c"
    }
}
```

