**Example 1: Getting function trigger list**



Input: 

```
tccli scf ListTriggers --cli-unfold-argument  \
    --FunctionName aaa\
    --Limit 2\
    --Order ASC
```

Output: 
```
{
    "Response": {
        "Triggers": [],
        "TotalCount": 0,
        "RequestID": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

