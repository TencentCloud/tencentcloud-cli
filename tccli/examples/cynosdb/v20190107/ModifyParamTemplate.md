**Example 1: 修改参数模板**

修改参数模板

Input: 

```
tccli cynosdb ModifyParamTemplate --cli-unfold-argument  \
    --TemplateDescription 勿删 \
    --TemplateId 94 \
    --ParamList.0.CurrentValue 1024 \
    --ParamList.0.ParamName query_cache_size \
    --TemplateName 5.7常用参数模板-勿删
```

Output: 
```
{
    "Response": {
        "RequestId": "916e8185-4749-45af-899f-e57043164675"
    }
}
```

