**Example 1: 批量初始化云数据库实例**



Input: 

```
tccli dcdb InitDCDBInstances --cli-unfold-argument  \
    --InstanceIds dcdbt-fdpjf5zh dcdbt-avw0207d\
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
            "dcdbt-fdpjf5zh",
            "dcdbt-avw0207d"
        ],
        "FlowIds": [
            3340,
            3341
        ]
    }
}
```

