**Example 1: 查询参数模板信息**

查询指定参数模板ID的模板信息

Input: 

```
tccli redis DescribeParamTemplateInfo --cli-unfold-argument  \
    --TemplateId crs-cfg-7mgt****
```

Output: 
```
{
    "Response": {
        "Description": "MyCustomParamTemplate",
        "Items": [
            {
                "CurrentValue": "",
                "Default": "\"\"",
                "Description": "commands in such config will not be allowed to run in this instance,you can config multi commands like this 'flushdb,keys'",
                "EnumValue": [
                    "flushall",
                    "flushdb",
                    "keys",
                    "hgetall",
                    "eval",
                    "evalsha",
                    "script"
                ],
                "Max": "",
                "Min": "",
                "Name": "disable-command-list",
                "NeedReboot": 0,
                "ParamType": "multi"
            },
            {
                "CurrentValue": "512",
                "Default": "512",
                "Description": "Hashes are encoded using a memory efficient data structure when they have a small number of entries",
                "EnumValue": null,
                "Max": "10000",
                "Min": "1",
                "Name": "hash-max-ziplist-entries",
                "NeedReboot": 0,
                "ParamType": "integer"
            },
            {
                "CurrentValue": "64",
                "Default": "64",
                "Description": "Hashes are encoded using a memory efficient data structure when the biggest entry does not exceed a given threshold",
                "EnumValue": null,
                "Max": "10000",
                "Min": "1",
                "Name": "hash-max-ziplist-value",
                "NeedReboot": 0,
                "ParamType": "integer"
            },
            {
                "CurrentValue": "10",
                "Default": "10",
                "Description": "The frequency at which Redis background tasks are performed. A higher value results in higher CPU consumption but smaller latency. We recommend that you do not specify a value larger than 100.",
                "EnumValue": null,
                "Max": "500",
                "Min": "1",
                "Name": "hz",
                "NeedReboot": 0,
                "ParamType": "integer"
            }
        ],
        "Name": "redis_automation_is_awesome_1",
        "ProductType": 2,
        "RequestId": "72881d6c-c2a0-42af-862a-a5de09de104d",
        "TemplateId": "crs-cfg-7mgt****",
        "TotalCount": 14
    }
}
```

