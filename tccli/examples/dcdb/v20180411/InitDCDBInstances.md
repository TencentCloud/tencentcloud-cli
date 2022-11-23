**Example 1: 批量初始化云数据库实例**



Input: 

```
tccli dcdb InitDCDBInstances --cli-unfold-argument  \
    --Params.0.Value 16384 \
    --Params.0.Param innodb_page_size \
    --Params.1.Value 1 \
    --Params.1.Param lower_case_table_names \
    --Params.2.Value utf8 \
    --Params.2.Param character_set_server \
    --InstanceIds dcdbt-avw0207d dcdbt-fdpjf5zh
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

