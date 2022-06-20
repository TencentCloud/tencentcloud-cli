**Example 1: 查询日志配置项列表**



Input: 

```
tccli tsf DescribeBusinessLogConfigs --cli-unfold-argument  \
    --Offset 0 \
    --Limit 50
```

Output: 
```
{
    "Response": {
        "RequestId": "7b9926c8-af66-4bdc-be70-612a9d1c1afc",
        "Result": {
            "TotalCount": 2,
            "Content": [
                {
                    "ConfigId": "apm-busi-log-cfg-qabp49vl",
                    "ConfigName": "default-log-config",
                    "ConfigPath": "PH_STARTUP_PATH/logs/*.log",
                    "ConfigDesc": null,
                    "ConfigTags": null,
                    "ConfigPipeline": "tsf-business-1251001060-qabp49vl",
                    "ConfigCreateTime": null,
                    "ConfigUpdateTime": null,
                    "ConfigSchema": {
                        "SchemaType": 0,
                        "SchemaContent": null,
                        "SchemaDateFormat": "YYYY-MM-dd HH:mm:ss.SSS",
                        "SchemaMultilinePattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}",
                        "SchemaCreateTime": "2019-04-17 17:00:37"
                    },
                    "ConfigAssociatedGroups": []
                },
                {
                    "ConfigId": "apm-busi-log-cfg-gyq883y5",
                    "ConfigName": "tsf_gateway",
                    "ConfigPath": "/logs/idreamsky-microservice-gateway/*.log",
                    "ConfigDesc": "/logs/idreamsky-microservice-gateway/*.log",
                    "ConfigTags": null,
                    "ConfigPipeline": "tsf-business-1251001060-gyq883y5",
                    "ConfigCreateTime": "2019-04-24 18:40:26",
                    "ConfigUpdateTime": "2019-04-24 18:40:26",
                    "ConfigSchema": {
                        "SchemaType": 0,
                        "SchemaContent": null,
                        "SchemaDateFormat": "YYYY-MM-dd HH:mm:ss.SSS",
                        "SchemaMultilinePattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}",
                        "SchemaCreateTime": "2019-04-24 18:40:26"
                    },
                    "ConfigAssociatedGroups": []
                }
            ]
        }
    }
}
```

