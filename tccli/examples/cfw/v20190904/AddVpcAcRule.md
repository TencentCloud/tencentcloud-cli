**Example 1: 添加VPC内网间规则**

添加VPC内网间规则

Input: 

```
tccli cfw AddVpcAcRule --cli-unfold-argument  \
    --Rules.0.OrderIndex 0 \
    --Rules.0.Enable 11 \
    --Rules.0.Protocol TCP \
    --Rules.0.SourceType SRC \
    --Rules.0.EdgeId cfws-xxxxxxxx \
    --Rules.0.EdgeName wo lie kai \
    --Rules.0.SourceContent 1.1.1.1 \
    --Rules.0.DestType 1 \
    --Rules.0.DestContent 2.2.2.2 \
    --Rules.0.RuleAction drop \
    --Rules.0.Uuid 0 \
    --Rules.0.DetectedTimes 0 \
    --Rules.0.Port 53 \
    --Rules.0.Description wo lie kai \
    --From src
```

Output: 
```
{
    "Response": {
        "RuleUuids": [
            8888,
            8889
        ],
        "RequestId": "9a86c4e3-b926-4244-919b-aba9a7e82686"
    }
}
```

