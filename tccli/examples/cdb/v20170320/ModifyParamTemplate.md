**Example 1: Modifying a parameter template**



Input: 

```
tccli cdb ModifyParamTemplate --cli-unfold-argument  \
    --TemplateId 11231 \
    --ParamList.0.Name auto_increment_increment \
    --ParamList.0.Value 1 \
    --ParamList.1.Name binlog_format \
    --ParamList.2.Value MIXED
```

Output: 
```
{
    "Response": {
        "RequestId": "756bb037-a44a-4b4f-abe0-6efd34a6c792"
    }
}
```

