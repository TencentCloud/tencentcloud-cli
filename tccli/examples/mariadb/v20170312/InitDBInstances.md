**Example 1: 批量初始化云数据库实例**



Input: 

```
tccli mariadb InitDBInstances --cli-unfold-argument  \
    --Params.0.Value 16384 \
    --Params.0.Param innodb_page_size \
    --Params.1.Value 1 \
    --Params.1.Param lower_case_table_names \
    --Params.2.Value utf8 \
    --Params.2.Param character_set_server \
    --InstanceIds tdsql-avw0207d tdsql-fdpjf5zh
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

