**Example 1: 调用示例**



Input: 

```
tccli wedata BatchPullModelData --cli-unfold-argument  \
    --Items.0.ResourceId res-0aa8c845 \
    --Items.0.DataModelKey e9306047ecd04a1417682215462799977cc29a9e3a761 \
    --Items.0.WorkspaceId 17678671667189298 \
    --Items.0.DashboardKey 798652297072988160 \
    --Items.0.Status PUBLISHED
```

Output: 
```
{
    "Response": {
        "Data": {
            "Data": [
                {
                    "CacheFileCosUrl": "/798652297072988160/51332cdbb0cf427a1768271900020924facecd643fd2d/DRAFT/d4f0766d3c3bd615f817fd40a045a8c6_700002164619_1768909933549.csv",
                    "DataModelKey": "51332cdbb0cf427a1768271900020924facecd643fd2d",
                    "DatasetVersion": 0,
                    "ErrorMsg": "",
                    "FieldInfoList": [
                        {
                            "CalcAggregation": "",
                            "CalcFormula": "",
                            "DataType": "DOUBLE",
                            "DataTypePrecision": 0,
                            "DataTypeScale": 0,
                            "Description": "",
                            "DisplayName": "longitude",
                            "FieldCategory": "",
                            "FieldType": "PHYSICAL",
                            "FormatRule": "",
                            "OriginalFields": "",
                            "PhysicalFieldName": "longitude"
                        }
                    ],
                    "Objects": "",
                    "ParameterList": [],
                    "Sql": "SELECT  * FROM DataLakeCatalog.xingyundong.point",
                    "Truncated": false
                }
            ],
            "ErrorMessage": "",
            "TranId": "89cf9c62c0978d4a47270ae88e1209b4",
            "TranStatus": "1"
        },
        "RequestId": "ca87cff9-0aa4-4b06-b12b-6bb3e38cae29"
    }
}
```

