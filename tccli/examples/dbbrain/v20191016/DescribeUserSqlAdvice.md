**Example 1: 获取SQL优化建议**

获取SQL优化建议。

Input: 

```
tccli dbbrain DescribeUserSqlAdvice --cli-unfold-argument  \
    --InstanceId cdb-c1nl9rpv \
    --SqlText 'select * from t1 where id in ( ? )'
```

Output: 
```
{
    "Response": {
        "RequestId": "e2a51350-8c9f-11eb-bc0f-c9f5ab88d057",
        "Advices": "[{\"TableName\": \"t1\", \"TableSchema\": \"test\", \"Keys\": [{\"SqlText\": \"alter table `test`.`t1` add index index_0(`id`);\"}]}]",
        "Comments": "[]",
        "Schema": "test",
        "Tables": "[{\"TableName\": \"t1\", \"TableSchema\": \"test\", \"TableDDL\": \"CREATE TABLE `test` (\n  `id` varchar(36) NOT NULL) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC\"}]",
        "SqlText": "select * from t1 where id in ( ? )",
        "SqlPlan": "{\"Before\": [{\"Format\": \"Table\", \"Data\": {\"Names\": [\"id\", \"select_type\", \"table\", \"partitions\", \"type\", \"possible_keys\", \"key\", \"key_len\", \"ref\", \"rows\", \"filtered\", \"Extra\"], \"Data\": [ [1, \"SIMPLE\", \"t1\", null, \"ALL\", null, null, null, null, 1530, 10, \"Using where\" ]]}}], \"After\": [{ \"Format\": \"Table\", \"Data\": {\"Names\": [\"id\", \"select_type\", \"table\", \"partitions\", \"type\", \"possible_keys\", \"key\", \"key_len\", \"ref\", \"rows\", \"filtered\", \"Extra\"], \"Data\": [[1, \"SIMPLE\", \"t1\", null, \"ref\", \"index_0\", \"index_0\", 1056, \"const\", 51, 100.00, null]]}}]}",
        "Cost": "{\"Before\": 0.1, \"After\": 0.03, \"Ratio\": 90.61}"
    }
}
```

**Example 2: 获取无需优化SQL的优化建议**

获取无需优化SQL的优化建议。

Input: 

```
tccli dbbrain DescribeUserSqlAdvice --cli-unfold-argument  \
    --InstanceId cdb-c1nl9rpv \
    --SqlText 'select * from t1 where id '
```

Output: 
```
{
    "Response": {
        "RequestId": "e2a51350-8c9f-11eb-bc0f-c9f5ab88d057",
        "Advices": "",
        "Comments": "",
        "Schema": "test",
        "Tables": "[{\"TableName\": \"t1\", \"TableSchema\": \"test\", \"TableDDL\": \"CREATE TABLE `test` (\n  `id` varchar(36) NOT NULL) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC\"}]",
        "SqlText": "select * from t1 where id in ( ? )",
        "SqlPlan": "",
        "Cost": ""
    }
}
```

