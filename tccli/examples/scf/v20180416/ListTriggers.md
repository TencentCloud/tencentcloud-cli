**Example 1: 获取函数触发器列表**



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
        "Triggers": [],
        "TotalCount": 0
    }
}
```

