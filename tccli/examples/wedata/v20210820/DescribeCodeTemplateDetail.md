**Example 1: 查看代码模版详情**

查看代码模版详情

Input: 

```
tccli wedata DescribeCodeTemplateDetail --cli-unfold-argument  \
    --CodeTemplateId 20250311155509313 \
    --ProjectId 1470547050521227264
```

Output: 
```
{
    "Response": {
        "Data": {
            "BrokerIp": "any",
            "CodeTemplateDesc": null,
            "CodeTemplateId": "20250311155509313",
            "CodeTemplateName": "copy11",
            "Ext": {
                "DryRunExtAttributes": null,
                "DryRunParameter": null,
                "Properties": [
                    {
                        "ParamKey": "bucket",
                        "ParamValue": "wedata-fusion-dev-1257305158"
                    },
                    {
                        "ParamKey": "ftp.file.name",
                        "ParamValue": "/datastudio/codeTemplate/1470547050521227264/copy11.py"
                    },
                    {
                        "ParamKey": "region",
                        "ParamValue": "ap-nanjing"
                    }
                ],
                "TaskId": "20250311155509313"
            },
            "FolderId": "",
            "FolderName": "",
            "InCharge": "kevinnie",
            "InChargeId": "100028578763",
            "LastUpdateTime": "2025-03-11 15:55:09",
            "ProjectId": "1470547050521227264",
            "ResourceGroup": null,
            "ScriptChange": true,
            "Submit": false,
            "TaskType": 30,
            "UpdateUser": "kevinnie",
            "UpdateUserId": "100028578763"
        },
        "RequestId": "9b5e61e9-0575-4c1e-9103-c1a1be7efc11"
    }
}
```

