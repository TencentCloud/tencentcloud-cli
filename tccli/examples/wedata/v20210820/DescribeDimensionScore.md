**Example 1: 查询维度评分**

查询维度评分

Input: 

```
tccli wedata DescribeDimensionScore --cli-unfold-argument  \
    --StatisticsDate 1647878400 \
    --ProjectId 1 \
    --DatasourceId qwe
```

Output: 
```
{
    "Response": {
        "Data": {
            "DimensionScoreList": [
                {
                    "Name": "abc",
                    "Weight": 0,
                    "UserId": 0,
                    "UserName": "abc",
                    "UpdateTime": 0,
                    "JoinTableNumber": 0,
                    "Score": 0
                }
            ]
        },
        "RequestId": "abc"
    }
}
```

