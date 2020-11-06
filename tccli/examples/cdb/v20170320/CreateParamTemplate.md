**Example 1: 创建参数模板**



Input: 

```
tccli cdb CreateParamTemplate --cli-unfold-argument  \
    --EngineVersion 5.7 \
    --Name test \
    --ParamList.0.Name auto_increment_increment \
    --ParamList.0.Value 1 \
    --ParamList.1.Name binlog_format \
    --ParamList.2.Value MIXED
```

Output: 
```
{
    "Response": {
        "RequestId": "756bb037-a44a-4b4f-abe0-6efd34a6c792",
        "TemplateId": 2333
    }
}
```

