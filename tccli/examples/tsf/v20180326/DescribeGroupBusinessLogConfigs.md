**Example 1: 查询分组关联日志配置项列表**



Input: 

```
tccli tsf DescribeGroupBusinessLogConfigs --cli-unfold-argument  \
    --GroupId group-maeqzl3a
```

Output: 
```
{
    "Response": {
        "RequestId": "cf6380d3-07c5-4607-babc-2490d3550bde",
        "Result": {
            "TotalCount": 1,
            "Content": [
                {
                    "ConfigId": "apm-busi-log-cfg-5yrdr8vj",
                    "ConfigName": "big-data-service",
                    "ConfigPath": "/tsf-iov-logs/big-data-service/root.log",
                    "ConfigDesc": "",
                    "ConfigTags": null,
                    "ConfigPipeline": "tsf-business-1254959430-5yrdr8vj",
                    "ConfigCreateTime": "2019-03-15 18:57:17",
                    "ConfigUpdateTime": "2019-03-15 18:57:17",
                    "ConfigSchema": {
                        "SchemaType": 0,
                        "SchemaContent": null,
                        "SchemaDateFormat": "YYYY-MM-dd HH:mm:ss.SSS",
                        "SchemaMultilinePattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}",
                        "SchemaCreateTime": "2019-03-15 18:57:17"
                    },
                    "ConfigAssociatedGroups": null
                }
            ]
        }
    }
}
```

