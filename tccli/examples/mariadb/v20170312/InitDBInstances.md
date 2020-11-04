**Example 1: 批量初始化云数据库实例**



Input: 

```
tccli mariadb InitDBInstances --cli-unfold-argument  \
    --InstanceIds tdsql-fdpjf5zh tdsql-avw0207d\
    --Params.0.Param lower_case_table_names\
    --Params.0.Value 1\
    --Params.1.Param innodb_page_size\
    --Params.1.Value 16384\
    --Params.2.Param character_set_server\
    --Params.2.Value utf8
```

Output: 
```
{
    "Response": {
        "RequestId": "d94ef093-ff84-4851-b2e0-a5c5920d618e",
        "InstanceIds": [
            "tdsql-fdpjf5zh",
            "tdsql-avw0207d"
        ],
        "FlowId": 3340
    }
}
```

