**Example 1: 查询某个参数模板支持添加的所有参数的信息**

无

Input: 

```
tccli postgres DescribeDefaultParameters --cli-unfold-argument  \
    --DBMajorVersion 13 \
    --DBEngine postgresql
```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "RequestId": "xx",
        "ParamInfoSet": [
            {
                "Advanced": false,
                "ClassificationCN": "AUTOVACUUM",
                "ClassificationEN": "Autovacuum",
                "CurrentValue": "",
                "DefaultValue": "-1",
                "EnumValue": null,
                "ID": 1409,
                "LastModifyTime": "",
                "Max": 10000,
                "Min": -1,
                "Name": "autovacuum_vacuum_cost_limit",
                "NeedReboot": false,
                "ParamDescriptionCH": "指定用于AUTOVACUUM操作中的代价限制值。如果指定-1（默认值），则使用vacuum_cost_limit值",
                "ParamDescriptionEN": "Vacuum cost amount available before napping, for autovacuum.",
                "ParamValueType": "integer",
                "SpecRelated": false,
                "StandbyRelated": 0,
                "Unit": ""
            },
            {
                "Advanced": false,
                "ClassificationCN": "复制",
                "ClassificationEN": "Replication",
                "CurrentValue": "",
                "DefaultValue": "27",
                "EnumValue": null,
                "ID": 1592,
                "LastModifyTime": "",
                "Max": 650,
                "Min": 27,
                "Name": "max_wal_senders",
                "NeedReboot": true,
                "ParamDescriptionCH": "wal发送进程的数量",
                "ParamDescriptionEN": "Sets the maximum number of simultaneously running WAL sender processes.",
                "ParamValueType": "integer",
                "SpecRelated": true,
                "StandbyRelated": 1,
                "Unit": ""
            }
        ]
    }
}
```

