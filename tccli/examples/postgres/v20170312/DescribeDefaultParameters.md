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
        "RequestId": "b6cf4dfc-09ce-4ee4-9c3e-0979e105bb4d",
        "TotalCount": 4,
        "ParamInfoSet": [
            {
                "Advanced": false,
                "ClassificationCN": "查询优化",
                "ClassificationEN": "Query Tuning",
                "CurrentValue": "",
                "DefaultValue": "500000",
                "EnumValue": [],
                "ID": 14092,
                "LastModifyTime": "",
                "Max": 123124123,
                "Min": -1,
                "Name": "jit_inline_above_cost",
                "NeedReboot": false,
                "ParamDescriptionCH": "设置JIT编译尝试内联函数和操作符的查询代价阈值，如果查询代价超过这个值，JIT编译就会尝试内联",
                "ParamDescriptionEN": "Perform JIT inlining if query is more expensive.-1 disables inlining.",
                "ParamValueType": "real",
                "SpecRelated": false,
                "SpecRelationSet": null,
                "StandbyRelated": 0,
                "Unit": "",
                "VersionRelationSet": null
            },
            {
                "Advanced": false,
                "ClassificationCN": "AUTOVACUUM",
                "ClassificationEN": "Autovacuum",
                "CurrentValue": "",
                "DefaultValue": "400000000",
                "EnumValue": [],
                "ID": 14131,
                "LastModifyTime": "",
                "Max": 2000000000,
                "Min": 10000,
                "Name": "autovacuum_multixact_freeze_max_age",
                "NeedReboot": true,
                "ParamDescriptionCH": "设置表上多事务场景下的最大年龄，达到这个阀值将触发 autovacuum进程，从而避免 wraparound.",
                "ParamDescriptionEN": "Multixact age at which to autovacuum a table to prevent multixact wraparound.",
                "ParamValueType": "integer",
                "SpecRelated": false,
                "SpecRelationSet": null,
                "StandbyRelated": 0,
                "Unit": "",
                "VersionRelationSet": null
            },
            {
                "Advanced": false,
                "ClassificationCN": "客户端连接默认值",
                "ClassificationEN": "Client Connection Defaults",
                "CurrentValue": "",
                "DefaultValue": "\"$user\", public",
                "EnumValue": [],
                "ID": 14173,
                "LastModifyTime": "",
                "Max": 0,
                "Min": 0,
                "Name": "search_path",
                "NeedReboot": false,
                "ParamDescriptionCH": "默认的search_path",
                "ParamDescriptionEN": "Sets the schema search order for names that are not schema-qualified.",
                "ParamValueType": "string",
                "SpecRelated": false,
                "SpecRelationSet": null,
                "StandbyRelated": 0,
                "Unit": "",
                "VersionRelationSet": null
            },
            {
                "Advanced": false,
                "ClassificationCN": "客户端连接默认值",
                "ClassificationEN": "Client Connection Defaults",
                "CurrentValue": "",
                "DefaultValue": "150000000",
                "EnumValue": [],
                "ID": 14175,
                "LastModifyTime": "",
                "Max": 2000000000,
                "Min": 0,
                "Name": "vacuum_multixact_freeze_table_age",
                "NeedReboot": false,
                "ParamDescriptionCH": "当表的pg_class.relfrozenxid域达到该设置指定的年龄时，VACUUM会执行一次全表扫描。 积极的扫描不同于常规的VACUUM，因为它会访问每个可能包含未冻结XID或MXID的页面，而不仅仅是那些可能包含死元组的页面",
                "ParamDescriptionEN": "Multixact age at which VACUUM should scan whole table to freeze tuples.",
                "ParamValueType": "integer",
                "SpecRelated": false,
                "SpecRelationSet": null,
                "StandbyRelated": 0,
                "Unit": "",
                "VersionRelationSet": null
            }
        ]
    }
}
```

