**Example 1: 获取示例问题**



Input: 

```
tccli wedata ListExternalQuestions --cli-unfold-argument  \
    --WorkspaceId 17625100163628872 \
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
    --TranId eac8b4f2-d54b-44dc-aeb0-9e5f7107b60e
```

Output: 
```
{
    "Response": {
        "Data": {
            "Questions": [
                {
                    "Question": "各产品类型销售额分布"
                }
            ],
            "TranId": "eac8b4f2-d54b-44dc-aeb0-9e5f7107b60e",
            "TranStatus": 1
        },
        "RequestId": "8b7aaacb-528c-4c7d-b0ce-a60aa7c44976"
    }
}
```

