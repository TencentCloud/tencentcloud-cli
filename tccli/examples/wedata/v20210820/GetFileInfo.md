**Example 1: 开发空间-获取数据开发脚本信息**

开发空间-获取数据开发脚本信息

Input: 

```
tccli wedata GetFileInfo --cli-unfold-argument  \
    --ProjectId 1486804694126882816 \
    --FilePath /datastudio/project/1486804694126882816/hui/111.sql
```

Output: 
```
{
    "Response": {
        "RequestId": "915a8a1f-04d8-463c-9687-9bd3a696b7ce",
        "UserFileInfo": {
            "Bucket": "wedata-fusion-dev-1257305158",
            "CreateTime": "2023-05-18 20:24:32",
            "DeleteName": null,
            "DeleteOwner": null,
            "ExtraInfo": [
                {
                    "ParamKey": "DatasourceType",
                    "ParamValue": "HIVE"
                },
                {
                    "ParamKey": "DatasourceId",
                    "ParamValue": "8445"
                },
                {
                    "ParamKey": "GroupId",
                    "ParamValue": ""
                },
                {
                    "ParamKey": "ResourceQueue",
                    "ParamValue": "root.default"
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
                }
            ],
            "FileExtensionType": "sql",
            "FileName": "111.sql",
            "LocalPath": "/datastudio/project/hui/111.sql",
            "LocalTempPath": null,
            "Md5Value": null,
            "Operator": null,
            "OperatorName": null,
            "Owner": "100028579427",
            "OwnerName": "hhhuilli",
            "PathDepth": 4,
            "ProjectId": "1486804694126882816",
            "Region": "ap-nanjing",
            "RemotePath": "/datastudio/project/1486804694126882816/hui/111.sql",
            "ResourceId": "3adddc91-21e2-494d-a207-1ee4c70d77f4",
            "Size": null,
            "Type": "project",
            "UpdateTime": "2023-05-18 20:25:55",
            "ZipPath": null
        }
    }
}
```

