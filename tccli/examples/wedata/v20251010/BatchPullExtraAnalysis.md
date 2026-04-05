**Example 1: 参数示例**



Input: 

```
tccli wedata BatchPullExtraAnalysis --cli-unfold-argument  \
    --Items.0.DataModelKey a3d5e1841768881416799aef7ed1c \
    --Items.0.ResourceId res-0aa8c845 \
    --Items.0.DragField.0.Code department \
    --Items.0.DragField.0.Alias 59e75fd8-f610-4d09-9c9d-08f0f5242520 \
    --Items.0.DragField.0.CalcType  \
    --Items.0.DragField.1.Code metric_1 \
    --Items.0.DragField.1.Alias 2057dac0-6de8-406f-abce-61d138170dbb \
    --Items.0.DragField.1.CalcType SUM \
    --Items.0.WhereList.Logic AND \
    --Items.0.WhereList.Conditions.0.Logic  \
    --Items.0.WhereList.Conditions.0.Left {"Type":"param","Code":"dep"} \
    --Items.0.WhereList.Conditions.0.Operator -is \
    --Items.0.WhereList.Conditions.0.Right {"Type":"value","Value":{"Type":"string","Values":["技术部"]}} \
    --Items.0.DashboardKey 801401584520798208 \
    --Items.0.Status DRAFT \
    --Items.0.WorkspaceId 17678671667189298 \
    --Items.0.Uuid a3d5e1841768881416799aef7ed1c_widget-f64277e3-0ac7-4399-8b1a-a88d41802bc2_aggregated \
    --DashboardKey 801401584520798208 \
    --WorkspaceId 17678671667189298
```

Output: 
```
{
    "Response": {
        "Data": {
            "Data": [
                {
                    "Objects": "[[\"技术部\",999949698]]",
                    "Sql": "SELECT\n    `department` AS A_DVA,\n    sum(`metric_1`) AS A_71D\nFROM (\n    SELECT *  FROM `DataLakeCatalog`.`xingyundong`.`one_million_rows_efficient` WHERE department = '技术部'\n) AS model\nGROUP BY department\n",
                    "Total": "0",
                    "ExtraParam": "",
                    "ResultDesc": [
                        {
                            "Key": "A_DVA",
                            "Alias": "59e75fd8-f610-4d09-9c9d-08f0f5242520"
                        },
                        {
                            "Key": "A_71D",
                            "Alias": "2057dac0-6de8-406f-abce-61d138170dbb"
                        }
                    ],
                    "Uuid": "a3d5e1841768881416799aef7ed1c_widget-f64277e3-0ac7-4399-8b1a-a88d41802bc2_aggregated",
                    "ErrorMsg": "",
                    "CacheFileCosUrl": ""
                }
            ],
            "TranId": "79b3afb0859741b660628519d143ca0d",
            "TranStatus": "1",
            "ErrorMessage": ""
        },
        "RequestId": "07c2f364-89db-4a9c-a479-52a7880a4e3d"
    }
}
```

