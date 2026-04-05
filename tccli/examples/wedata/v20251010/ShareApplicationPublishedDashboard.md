**Example 1: 分享嵌出、仪表盘发布态信息**



Input: 

```
tccli wedata ShareApplicationPublishedDashboard --cli-unfold-argument  \
    --WorkspaceId 17663856806379896 \
    --AccessKey 797848762287833088
```

Output: 
```
{
    "Response": {
        "Data": {
            "AccessKey": "797848762287833088",
            "DashboardVersion": 0,
            "DatasetOrderList": [
                "7de5efd89b97479217680299904139f44838600d8ee0b"
            ],
            "Datasets": [
                {
                    "Catalog": "c4",
                    "CustomSql": "SELECT * FROM `c4`.`default`.`lingshou_202601081143`",
                    "DataFrom": "SQL",
                    "DatasetVersion": 5,
                    "DatasourceType": "",
                    "Description": "",
                    "DisplayName": "point",
                    "FieldInfoList": [
                        {
                            "CalcAggregation": "",
                            "CalcFormula": "",
                            "DataType": "DATE",
                            "DataTypePrecision": 0,
                            "DataTypeScale": 0,
                            "Description": "",
                            "DisplayName": "time",
                            "FieldCategory": "DIMENSION",
                            "FieldType": "PHYSICAL",
                            "FormatRule": "yyyy-MM-dd",
                            "Key": "1dc5f8eb8c2c4c6a17680337827818ab9292cb340b3ad",
                            "OriginalFields": "",
                            "PhysicalFieldName": "time"
                        }
                    ],
                    "Key": "7de5efd89b97479217680299904139f44838600d8ee0b",
                    "ModelType": "CUSTOM",
                    "ParameterList": [],
                    "Schema": "default",
                    "TableName": ""
                }
            ],
            "DisplayName": "tiny_test",
            "ExecuteResourceId": "res-4d5a8928",
            "IsFavorite": false,
            "PageOrderList": [
                "313f6f3fb4b647da17680299689769e5e0f71e245c60f"
            ],
            "Pages": [
                {
                    "CustomerRefId": "6c7b06f0a708405290c33b80aec90fe9",
                    "DisplayName": "无标题页面",
                    "PageAccessKey": "313f6f3fb4b647da17680299689769e5e0f71e245c60f",
                    "PageLayout": "[{\"w\":5,\"h\":6,\"x\":1,\"y\":0,\"i\":\"widget-6aceb04d-2327-4df2-8998-de78ad934421\",\"minW\":1,\"maxW\":null,\"minH\":1,\"maxH\":null,\"moved\":false,\"static\":false},{\"w\":5,\"h\":6,\"x\":1,\"y\":6,\"i\":\"widget-adb421ee-e5ae-47a0-b507-775c67d1ec68\",\"minW\":1,\"maxW\":null,\"minH\":1,\"maxH\":null,\"moved\":false,\"static\":false}]",
                    "PageType": "PAGE_TYPE_NORMAL",
                    "PageVersion": 17,
                    "Widgets": [
                        {
                            "CustomerRefId": "widget-6aceb04d-2327-4df2-8998-de78ad934421",
                            "WidgetAccessKey": "e27266cc1b0d4a401768033187725baa845a5915b3edf",
                            "WidgetOption": "{\"visualization\":\"bar\",\"datasetName\":\"7de5efd89b97479217680299904139f44838600d8ee0b\",\"showAiAssistant\":false,\"x\":{\"selectFields\":[{\"Key\":\"1dc5f8eb8c2c4c6a17680337827818ab9292cb340b3ad\",\"DisplayName\":\"time\",\"Description\":\"\",\"FieldType\":\"PHYSICAL\",\"PhysicalFieldName\":\"time\",\"DataType\":\"DATE\",\"DataTypePrecision\":0,\"DataTypeScale\":0,\"CalcFormula\":\"\",\"OriginalFields\":\"\",\"FieldCategory\":\"\",\"FormatRule\":\"yyyy-MM-dd\",\"CalcAggregation\":\"\",\"Alias\":\"ac2da37f-d426-4ee9-9877-9c65d95525b1\",\"Aggregation\":\"day\"}],\"setting\":{\"axisTitle\":\"\",\"showAxisTitle\":true,\"showAxisValue\":true,\"showAxisCategory\":true,\"fieldTitle\":\"\",\"defaultCategoryCount\":\"all\",\"labelAngle\":\"auto\",\"sortType\":\"a-z\",\"dataType\":\"continuous\",\"isOpenDualAxis\":false},\"format\":{\"activeTab\":\"axis\",\"formatType\":\"auto\",\"numberType\":\"default\",\"abbreviation\":\"abbreviate\",\"decimalPlaces\":\"max\"}},\"y\":{\"selectFields\":[{\"Key\":\"a3084e0c74f44cf51768033782786ae84d0027e1bd4b2\",\"DisplayName\":\"sales_volume\",\"Description\":\"\",\"FieldType\":\"PHYSICAL\",\"PhysicalFieldName\":\"sales_volume\",\"DataType\":\"INT\",\"DataTypePrecision\":0,\"DataTypeScale\":0,\"CalcFormula\":\"\",\"OriginalFields\":\"\",\"FieldCategory\":\"\",\"FormatRule\":\"\",\"CalcAggregation\":\"\",\"Alias\":\"a91f3ccc-161e-4b0e-9e05-1eae6f5f88b3\",\"Aggregation\":\"sum\"}]},\"color\":{\"singleColor\":\"#0DAEEA\",\"piecewiseColor\":{},\"byYColor\":[],\"gradientColor\":{\"fieldName\":\"\",\"type\":\"continuous\",\"show\":true,\"text\":[],\"align\":\"right\",\"orient\":\"horizontal\",\"colorRamp\":{\"type\":\"default\",\"name\":\"blues\"},\"min\":null,\"max\":null,\"range\":[null,null],\"inRange\":{\"color\":[\"#eff3ff\",\"#2171b5\"]}},\"pointMapSingleColor\":[{\"inRange\":{\"color\":[\"#066EFF\"]}}],\"pointMapGradientColor\":{\"orient\":\"horizontal\",\"calculable\":true,\"left\":0,\"bottom\":0,\"dimension\":3,\"min\":null,\"max\":null,\"inRange\":{\"color\":[\"#eff3ff\",\"#2171b5\"]}},\"currentColorConfig\":\"singleColor\"}}",
                            "WidgetRid": "widget-6aceb04d-2327-4df2-8998-de78ad934421",
                            "WidgetType": "bar",
                            "WidgetVersion": 8
                        }
                    ]
                }
            ],
            "PublishTime": "1768037670348",
            "PublishUin": "700002164618",
            "UiSettings": ""
        },
        "RequestId": "b12505ae-5d8d-4164-9eab-25e28ba8b50e"
    }
}
```

