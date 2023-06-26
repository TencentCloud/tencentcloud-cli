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
        "RequestId": "7cb20a58-a110-48ed-b539-0807e9af05d6",
        "Data": {
            "CompositeScore": 17.76,
            "TotalTableNumber": 1,
            "ScoringDistribution": [
                {
                    "Level": 1,
                    "TableNumber": 1,
                    "Scale": 0
                },
                {
                    "Level": 2,
                    "TableNumber": 1,
                    "Scale": 0
                },
                {
                    "Level": 3,
                    "TableNumber": 0,
                    "Scale": 0
                },
                {
                    "Level": 4,
                    "TableNumber": 0,
                    "Scale": 0
                },
                {
                    "Level": 5,
                    "TableNumber": 1,
                    "Scale": 100
                }
            ]
        }
    }
}
```

