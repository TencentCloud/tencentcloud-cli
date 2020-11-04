**Example 1: 创建新的触发器**

用户使用该函数创建新的触发器

Input: 

```
tccli scf CreateTrigger --cli-unfold-argument  \
    --FunctionName <FunctionName>\
    --TriggerName <TriggerName>\
    --Type timer\
    --TriggerDesc */2****
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

