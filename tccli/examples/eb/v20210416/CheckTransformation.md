**Example 1: 检查转换器**



Input: 

```
tccli eb CheckTransformation --cli-unfold-argument  \
    --Input {"data":{"msgBody":"{\"city\":\"shenzhen\",\"temp\":32,\"weather\":\"sunny\"}"}} \
    --Transformations.0.Extraction.ExtractionInputPath $.data.msgBody \
    --Transformations.0.Extraction.Format JSON \
    --Transformations.0.Extraction.TextParams.Separator : \
    --Transformations.0.Extraction.TextParams.Regex shenzhen \
    --Transformations.0.EtlFilter.Filter {"city":[{"contain":"shen"}]} \
    --Transformations.0.Transform.OutputStructs.0.Key city \
    --Transformations.0.Transform.OutputStructs.0.Value $.city \
    --Transformations.0.Transform.OutputStructs.0.ValueType JSONPATH \
    --Transformations.0.Transform.OutputStructs.1.Key const \
    --Transformations.0.Transform.OutputStructs.1.Value 11 \
    --Transformations.0.Transform.OutputStructs.1.ValueType NUMBER \
    --Transformations.0.Transform.OutputStructs.2.Key sdate \
    --Transformations.0.Transform.OutputStructs.2.Value date \
    --Transformations.0.Transform.OutputStructs.2.ValueType SYS_VARIABLE
```

Output: 
```
{
    "Response": {
        "RequestId": "589fd30c-49c9-11ec-9ad1-5254006e5bc5",
        "Output": "{\"sdate\":\"2021-11-20T14:16:06+08:00\",\"city\":\"shenzhen\",\"const\":11}"
    }
}
```

