**Example 1: 添加互联网边界规则**



Input: 

```
tccli cfw AddAcRule --cli-unfold-argument  \
    --OrderIndex -1 \
    --Description api test1 \
    --SourceType location \
    --SourceContent cq50,sh31,tj12,bj11 \
    --DestType net \
    --DestContent 0.0.0.0/0 \
    --Enable true \
    --Direction in \
    --RuleAction accept \
    --Port -1/-1 \
    --Protocol tcp \
    --ApplicationName 
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

