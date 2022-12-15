**Example 1: 查询参数模板详情**

无

Input: 

```
tccli postgres DescribeParameterTemplateAttributes --cli-unfold-argument  \
    --TemplateId c0456ace-31d1-54b1-a270-befa6bf960a5
```

Output: 
```
{
    "Response": {
        "DBEngine": "postgresql",
        "DBMajorVersion": "12",
        "ParamInfoSet": [
            {
                "Advanced": false,
                "ClassificationCN": "WAL",
                "ClassificationEN": "Write-Ahead Log",
                "CurrentValue": "logical",
                "DefaultValue": "replica",
                "EnumValue": [
                    "replica",
                    "logical"
                ],
                "ID": 854,
                "LastModifyTime": "",
                "Max": 0,
                "Min": 0,
                "Name": "wal_level",
                "NeedReboot": true,
                "ParamDescriptionCH": "此参数决定记录到日志的信息，不允许设置为minimal",
                "ParamDescriptionEN": "Set the level of information written to the WAL.",
                "ParamValueType": "enum",
                "SpecRelated": false,
                "StandbyRelated": 0,
                "Unit": ""
            },
            {
                "Advanced": false,
                "ClassificationCN": "资源使用",
                "ClassificationEN": "Resource Usage",
                "CurrentValue": "12",
                "DefaultValue": "8",
                "EnumValue": null,
                "ID": 755,
                "LastModifyTime": "",
                "Max": 262143,
                "Min": 0,
                "Name": "max_worker_processes",
                "NeedReboot": true,
                "ParamDescriptionCH": "系统能够支持的后台进程的最大数量",
                "ParamDescriptionEN": "Maximum number of concurrent worker processes.",
                "ParamValueType": "integer",
                "SpecRelated": true,
                "StandbyRelated": 1,
                "Unit": ""
            }
        ],
        "RequestId": "e4f0f472-8bef-4404-b3fa-57ed6b6378b8",
        "TemplateDescription": "test-modify",
        "TemplateId": "c0456ace-31d1-54b1-a270-befa6bf960a5",
        "TemplateName": "test-modify_1",
        "TotalCount": 2
    }
}
```

