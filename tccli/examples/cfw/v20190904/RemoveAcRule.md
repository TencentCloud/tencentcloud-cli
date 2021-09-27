**Example 1: 删除互联网边界规则**



Input: 

```
tccli cfw RemoveAcRule --cli-unfold-argument  \
    --RuleUuid 8888
```

Output: 
```
{
    "Response": {
        "RuleUuid": 8888,
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03",
        "ReturnCode": 0,
        "ReturnMsg": "success"
    }
}
```

