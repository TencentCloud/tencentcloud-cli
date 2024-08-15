**Example 1: 获取查询信息**



Input: 

```
tccli dlc DescribeQuery --cli-unfold-argument  \
    --TaskId 9e20f9c021cb11ec835f5254006c64af
```

Output: 
```
{
    "Response": {
        "RequestId": "9328049f-30bc-4feb-aecf-e3b4ff2d1b00",
        "TaskId": "9e20f9c021cb11ec835f5254006c64af",
        "SQL": "SELECT * FROM `auth_test`.`hive_test` LIMIT 10",
        "SQLType": "DDL",
        "State": 2,
        "DataSet": "{\"Schema\":[\"name\",\"age\"],\"Data\":[{\"name\":\"29\",\"age\":\"Michael\"}]}"
    }
}
```

