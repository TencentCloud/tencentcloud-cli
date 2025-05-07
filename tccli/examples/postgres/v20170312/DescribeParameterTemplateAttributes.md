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
                "VersionRelationSet": [],
                "SpecRelated": false,
                "StandbyRelated": 0,
                "Unit": "",
                "SpecRelationSet": []
            }
        ],
        "RequestId": "e4f0f472-8bef-4404-b3fa-57ed6b6378b8",
        "TemplateDescription": "test-modify",
        "TemplateId": "c0456ace-31d1-54b1-a270-befa6bf960a5",
        "TemplateName": "test-modify_1",
        "TotalCount": 1
    }
}
```

