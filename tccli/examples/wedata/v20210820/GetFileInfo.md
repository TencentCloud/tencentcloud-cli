**Example 1: 开发空间-获取数据开发脚本信息**

开发空间-获取数据开发脚本信息

Input: 

```
tccli wedata GetFileInfo --cli-unfold-argument  \
    --ProjectId 1470547050521227264 \
    --FilePath /datastudio/project/1470547050521227264/test.sql
```

Output: 
```
{
    "Response": {
        "RequestId": "b65844ce-b928-4c45-97c6-4c97505c98c9",
        "UserFileInfo": {
            "Bucket": "wedata-fusion-dev-1257305158",
            "CreateTime": "2025-08-08 11:34:54",
            "DeleteName": null,
            "DeleteOwner": null,
            "EncodeExtraInfo": "eyJEYXRhc291cmNlVHlwZSI6IkhJVkUiLCJEYXRhc291cmNlSWQiOjYxNTIzLCJHcm91cElkIjoiMjAyNDAyMjIyMTI3MTk4MzM3NDMiLCJSZXNvdXJjZVF1ZXVlIjoiIiwiQ29tcHV0ZVJlc291cmNlIjoiIiwiRGF0YWJhc2VOYW1lIjoiIiwiQ29uZlBhcmFtcyI6eyJSZXNvdXJjZUNvbmZQYXJhbXMiOnt9fSwiQ29tcHV0ZVJlc291cmNlVHlwZSI6IiJ9",
            "ExtraInfo": [
                {
                    "ParamKey": "DatasourceType",
                    "ParamValue": "HIVE"
                },
                {
                    "ParamKey": "DatasourceId",
                    "ParamValue": "61523"
                },
                {
                    "ParamKey": "GroupId",
                    "ParamValue": "20240222212719833743"
                },
                {
                    "ParamKey": "ResourceQueue",
                    "ParamValue": ""
                },
                {
                    "ParamKey": "ComputeResource",
                    "ParamValue": ""
                },
                {
                    "ParamKey": "DatabaseName",
                    "ParamValue": ""
                },
                {
                    "ParamKey": "ConfParams",
                    "ParamValue": "&&&ResourceConfParams=&&&}}"
                },
                {
                    "ParamKey": "ComputeResourceType",
                    "ParamValue": ""
                }
            ],
            "FileExtensionType": "sql",
            "FileName": "test.sql",
            "LocalPath": "/datastudio/project/test.sql",
            "LocalTempPath": null,
            "Md5Value": null,
            "Operator": "100042680225",
            "OperatorName": "jasonzcwang",
            "Owner": "100042680225",
            "OwnerName": "jasonzcwang",
            "PathDepth": 3,
            "ProjectId": "1470547050521227264",
            "Region": "ap-nanjing",
            "RemotePath": "/datastudio/project/1470547050521227264/test.sql",
            "ResourceId": "42f78795-2c79-4507-9ce2-eb9d8e177d8e",
            "Size": null,
            "Type": "project",
            "UpdateTime": "2025-08-08 11:35:23",
            "ZipPath": null
        }
    }
}
```

