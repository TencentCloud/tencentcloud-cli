**Example 1: 查询维度评分**

查询维度评分

Input: 

```
tccli wedata DescribeDimensionScore --cli-unfold-argument  \
    --ProjectId 1547781656817664 \
    --StatisticsDate 1712592000 \
    --DatasourceId 567890 \
    --Filters.0.Name DatabasesIds \
    --Filters.0.Values 78tygi2q0384yehuif \
    --Filters.1.Name TableIds \
    --Filters.1.Values 80yhuqp3egaw-fdiphj
```

Output: 
```
{
    "Response": {
        "Data": {
            "DimensionScoreList": [
                {
                    "JoinTableNumber": 0,
                    "Name": "一致性",
                    "Score": 0,
                    "UpdateTime": 1695718800000,
                    "UserId": 12941056,
                    "UserName": "AUTO_TEST",
                    "Weight": 10
                },
                {
                    "JoinTableNumber": 0,
                    "Name": "准确性",
                    "Score": 0,
                    "UpdateTime": 1678914216000,
                    "UserId": null,
                    "UserName": "系统默认",
                    "Weight": 25
                },
                {
                    "JoinTableNumber": 0,
                    "Name": "及时性",
                    "Score": 0,
                    "UpdateTime": 1678914216000,
                    "UserId": null,
                    "UserName": "系统默认",
                    "Weight": 25
                },
                {
                    "JoinTableNumber": 0,
                    "Name": "唯一性",
                    "Score": 0,
                    "UpdateTime": 1678914216000,
                    "UserId": null,
                    "UserName": "系统默认",
                    "Weight": 15
                },
                {
                    "JoinTableNumber": 0,
                    "Name": "完整性",
                    "Score": 0,
                    "UpdateTime": 1697029625000,
                    "UserId": 10411056,
                    "UserName": "AUTO_TEST",
                    "Weight": 20
                },
                {
                    "JoinTableNumber": 0,
                    "Name": "有效性",
                    "Score": 0,
                    "UpdateTime": 1678914216000,
                    "UserId": null,
                    "UserName": "系统默认",
                    "Weight": 15
                }
            ]
        },
        "RequestId": "e447b6ad-c3c3-44b5-b473-dbfc39591f93"
    }
}
```

