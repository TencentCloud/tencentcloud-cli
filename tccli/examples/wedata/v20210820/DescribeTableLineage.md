**Example 1: 表血缘信息**

表血缘信息

Input: 

```
tccli wedata DescribeTableLineage --cli-unfold-argument  \
    --Direction INPUT \
    --Data.MetastoreType HIVE \
    --Data.PrefixPath  \
    --Data.TableId JqDviGd3SJKP1DzlUbbccdd \
    --IgnoreTemp True \
    --InputDepth 1 \
    --OutputDepth 1
```

Output: 
```
{
    "Response": {
        "RequestId": "e269b107-113c-4e21-a268-75da4abbf9a4",
        "TableLineage": {
            "ChannelType": null,
            "ChildSet": null,
            "CreateTime": "",
            "DatabaseId": "1-zla91ZRLOUNMC9aabbcc",
            "DatabaseName": "box",
            "DatasourceId": "9323",
            "DatasourceName": "hive_emr-cvdaabbcc",
            "Description": "",
            "DisplayType": null,
            "DownStreamCount": 0,
            "ExtParams": [],
            "Id": null,
            "MetastoreType": null,
            "MetastoreTypeName": null,
            "ModifyTime": "",
            "Params": [],
            "ParentSet": null,
            "PrefixPath": "",
            "ProjectId": null,
            "QualifiedName": null,
            "TableId": "JqDviGd3SJKP1DzlUXaabbcc",
            "TableName": "0210_biao1",
            "TableType": null,
            "Tasks": [],
            "UpStreamCount": 0
        }
    }
}
```

**Example 2: 表血缘信息2**

表血缘信息2

Input: 

```
tccli wedata DescribeTableLineage --cli-unfold-argument  \
    --Direction OUTPUT \
    --InputDepth 1 \
    --OutputDepth 1 \
    --Data.MetastoreType HIVE \
    --Data.PrefixPath  \
    --Data.TableId Qvkit5nqSYqTmn3IAQrpYQ \
    --IgnoreTemp True
```

Output: 
```
{
    "Response": {
        "RequestId": "ca391b2a-be9d-4412-a699-98ecd6479a06",
        "TableLineage": {
            "ChannelType": null,
            "ChildSet": "[{\"ProjectId\":\"180589\",\"Params\":[],\"Id\":\"5be96928b52c8db567cbe90d7bac1e10\",\"MetastoreType\":\"HIVE\",\"MetastoreTypeName\":\"HIVE\",\"TableType\":\"TABLE\",\"TableName\":\"student_table_copy\",\"Guid\":\"u_bLpJpLQ06sUMCkZNhSyQ\",\"QualifiedName\":\"guldan_ods.student_table_copy\",\"DownStreamCount\":1,\"UpStreamCount\":1,\"Description\":\"\",\"PrefixPath\":\"f208bc03544797d08ef9d9eca39bdafb@5be96928b52c8db567cbe90d7bac1e10\",\"CreateTime\":\"2023-09-14 23:22:40\",\"ModifyTime\":\"2024-03-06 19:40:40\",\"Tasks\":[\"6202404301808319831\",\"6202404301730219946\",\"6202309150003168701\",\"6202311061201443094\",\"20230824011039676\",\"6202408030252238415\",\"6202404301807395098\"],\"SyncTasks\":\"[]\",\"ParentSet\":[],\"ChildSet\":[],\"ExtParams\":[{\"Name\":\"flag\",\"Value\":\"false\"},{\"Name\":\"nodeid\",\"Value\":\"fef4da76-c810-4fa7-b26b-b257c4c322dd\"}],\"DatasourceId\":\"43392\"}]",
            "CreateTime": "2023-09-14 23:22:40",
            "DatabaseId": "a2x29pNmQbysZRaTCoZaUA",
            "DatabaseName": "guldan_ods",
            "DatasourceId": "43392",
            "DatasourceName": "hive_emr-foxwi67c",
            "Description": "",
            "DisplayType": null,
            "DownStreamCount": 1,
            "EngineType": null,
            "ExtParams": [
                {
                    "Name": "flag",
                    "Value": "true"
                },
                {
                    "Name": "nodeid",
                    "Value": "dfde51fb-dd33-48a3-ab26-22ea610ba7b3"
                }
            ],
            "Id": "f208bc03544797d08ef9d9eca39bdafb",
            "MetastoreType": "HIVE",
            "MetastoreTypeName": "HIVE",
            "ModifyTime": "2024-03-06 19:40:40",
            "Params": [],
            "ParentSet": "",
            "PrefixPath": "f208bc03544797d08ef9d9eca39bdafb",
            "ProjectId": "180589",
            "QualifiedName": "guldan_ods.student_table",
            "TableId": "Qvkit5nqSYqTmn3IAQrpYQ",
            "TableName": "student_table",
            "TableType": "TABLE",
            "Tasks": [
                "6202404301808319831",
                "6202404301730219946",
                "6202309150003168701",
                "6202311061201443094",
                "20230824011039676",
                "6202408030252238415",
                "6202404301807395098"
            ],
            "UpStreamCount": 0
        }
    }
}
```

