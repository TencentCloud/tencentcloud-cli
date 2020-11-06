**Example 1: 查询数据库表**



Input: 

```
tccli cdb DescribeTables --cli-unfold-argument  \
    --InstanceId cdb-c1nl9rpv \
    --Database mysql
```

Output: 
```
{
    "Response": {
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7",
        "TotalCount": 10,
        "Items": [
            "CHARACTER_SETS",
            "COLLATIONS",
            "COLLATION_CHARACTER_SET_APPLICABILITY",
            "COLUMNS",
            "COLUMN_PRIVILEGES",
            "ENGINES",
            "EVENTS",
            "FILES",
            "GLOBAL_STATUS",
            "GLOBAL_VARIABLES"
        ]
    }
}
```

