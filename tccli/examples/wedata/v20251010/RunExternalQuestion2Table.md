**Example 1: 自然语言生成图表-组件调用**



Input: 

```
tccli wedata RunExternalQuestion2Table --cli-unfold-argument  \
    --WorkspaceId 17625100163628872 \
    --DatasetName 64db15f45110434d17671768471829a8bde36c6e1505b \
    --FieldsInfo.0.Field product_type \
    --FieldsInfo.0.FieldCN 产品类型 \
    --FieldsInfo.0.FieldType string \
    --FieldsInfo.0.IsFormula False \
    --FieldsInfo.0.IsAggregation False \
    --FieldsInfo.0.Formula  \
    --FieldsInfo.0.FormatRule  \
    --FieldsInfo.0.Aggregation  \
    --FieldsInfo.0.Key  \
    --LanguageConfig Chinese \
    --Question 各产品类型的销售额分布 \
    --Stream False \
    --TranId 285750211a73253aec96b536fb728dc9
```

Output: 
```
{
    "Response": {
        "Data": {
            "DatasetName": "64db15f45110434d17671768471829a8bde36c6e1505b",
            "FrontProtocol": "{\"visualization\":\"pie\",\"datasetName\":\"64db15f45110434d17671768471829a8bde36c6e1505b\",\"angle\":{\"selectFields\":[{\"Key\":\"\",\"DisplayName\":\"销售额\",\"Description\":\"\",\"FieldType\":\"CALCULATED\",\"PhysicalFieldName\":\"sales_amount\",\"DataType\":\"DECIMAL\",\"DataTypePrecision\":0,\"DataTypeScale\":0,\"CalcFormula\":\"\",\"CalcAggregation\":\"\",\"OriginalFields\":\"\",\"FieldCategory\":\"MEASURE\",\"FormatRule\":\"\",\"Alias\":\"20c95f89-a391-431d-8604-63743892bbf9\",\"Aggregation\":\"sum\"}]},\"color\":{\"selectFields\":[{\"Key\":\"\",\"DisplayName\":\"产品类型\",\"Description\":\"\",\"FieldType\":\"CALCULATED\",\"PhysicalFieldName\":\"product_type\",\"DataType\":\"STRING\",\"DataTypePrecision\":0,\"DataTypeScale\":0,\"CalcFormula\":\"\",\"CalcAggregation\":\"\",\"OriginalFields\":\"\",\"FieldCategory\":\"DIMENSION\",\"FormatRule\":\"\",\"Alias\":\"a38bf46d-6369-4bb2-ae8e-7d3c6cf8072c\"}]},\"frame\":{\"showTitle\":true,\"showDescription\":false,\"title\":\"各产品类型销售额分布\",\"description\":\"根据用户查询生成的可视化图表组件\"}}",
            "TranId": "285750211a73253aec96b536fb728dc9",
            "TranStatus": 1
        },
        "RequestId": "9cab3699-f4c6-4a69-8114-897794ee1266"
    }
}
```

