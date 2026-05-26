**Example 1: 创建/修改脱敏规则**



Input: 

```
tccli emr IssueMaskRulesSTD --cli-unfold-argument  \
    --InstanceId 实例ID \
    --OperateType ADD
```

Output: 
```
{
    "Response": {
        "RequestId": "2b41c59d-93c8-43e2-a2f0-6c5df9735d21",
        "Data": [
            {
                "Item": "default.a.c",
                "Result": true
            },
            {
                "Item": "abc",
                "Result": "Duplicated"
            }
        ]
    }
}
```

