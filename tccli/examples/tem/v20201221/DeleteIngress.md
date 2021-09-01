**Example 1: 查询 Ingress 规则**

查询 Ingress 规则

Input: 

```
tccli tem DeleteIngress --cli-unfold-argument  \
    --NamespaceId cls-xxx \
    --EksNamespace default \
    --Name xxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "81f74023-563c-437d-abf7-8139449ef178",
        "Result": true
    }
}
```

