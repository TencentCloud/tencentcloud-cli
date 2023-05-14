**Example 1: 创建新的触发器**

用户使用该函数创建新的触发器

Input: 

```
tccli scf CreateTrigger --cli-unfold-argument  \
    --FunctionName <FunctionName> \
    --TriggerName <TriggerName> \
    --Type timer \
    --TriggerDesc */2****
```

Output: 
```
{
    "Response": {
        "TriggerInfo": {
            "AddTime": "2021-06-09 16:07:18",
            "AvailableStatus": "Available",
            "BindStatus": "on",
            "CustomArgument": "",
            "Description": "",
            "Enable": 0,
            "ModTime": "2021-08-31 21:45:32",
            "Qualifier": "$DEFAULT",
            "ResourceId": "XXX",
            "TriggerAttribute": "single",
            "TriggerDesc": "{\"cron\":\"0 */2 * * * * *\"}",
            "TriggerName": "TriggerName",
            "Type": "timer"
        },
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

