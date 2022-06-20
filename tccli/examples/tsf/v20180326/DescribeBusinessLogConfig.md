**Example 1: 查询业务日志配置项信息**



Input: 

```
tccli tsf DescribeBusinessLogConfig --cli-unfold-argument  \
    --ConfigId apm-busi-log-cfg-qv3me6a7
```

Output: 
```
{
    "Response": {
        "RequestId": "7a20c18e-c171-4f5a-ac94-71aa92035216",
        "Result": {
            "ConfigId": "apm-busi-log-cfg-qv3me6a7",
            "ConfigName": "default-log-config",
            "ConfigPath": "PH_STARTUP_PATH/logs/*.log",
            "ConfigDesc": null,
            "ConfigTags": null,
            "ConfigPipeline": "tsf-business-1259302344-qv3me6a7",
            "ConfigCreateTime": null,
            "ConfigUpdateTime": null,
            "ConfigSchema": {
                "SchemaType": 0,
                "SchemaContent": null,
                "SchemaDateFormat": "YYYY-MM-dd HH:mm:ss.SSS",
                "SchemaMultilinePattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}",
                "SchemaCreateTime": "2019-05-27 11:16:59"
            },
            "ConfigAssociatedGroups": []
        }
    }
}
```

