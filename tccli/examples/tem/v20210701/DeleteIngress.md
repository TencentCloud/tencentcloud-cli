**Example 1: 删除 Ingress 规则**

删除 Ingress 规则

Input: 

```
tccli tem DeleteIngress --cli-unfold-argument  \
    --EnvironmentId en-xxxxxx \
    --ClusterNamespace default \
    --SourceChannel 0 \
    --IngressName ingress-name
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

