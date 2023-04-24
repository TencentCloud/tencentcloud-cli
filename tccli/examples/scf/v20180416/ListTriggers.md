**Example 1: 获取函数触发器列表**

获取函数触发器列表

Input: 

```
tccli scf ListTriggers --cli-unfold-argument  \
    --FunctionName aaa \
    --Limit 2 \
    --Order ASC
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Triggers": [
            {
                "Enable": 1,
                "Qualifier": "abc",
                "TriggerName": "abc",
                "Type": "abc",
                "TriggerDesc": "abc",
                "AvailableStatus": "abc",
                "CustomArgument": "abc",
                "Description": "abc",
                "AddTime": "2020-09-22 00:00:00",
                "ModTime": "2020-09-22 00:00:00",
                "ResourceId": "abc",
                "BindStatus": "abc",
                "TriggerAttribute": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

