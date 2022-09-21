**Example 1: 创建参数模板**



Input: 

```
tccli cdb CreateParamTemplate --cli-unfold-argument  \
    --TemplateType HIGH_STABILITY \
    --Name test \
    --ParamList.0.CurrentValue MIXED \
    --ParamList.0.Name binlog_format \
    --ParamList.1.CurrentValue 1 \
    --ParamList.1.Name auto_increment_increment \
    --EngineVersion 5.7
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

