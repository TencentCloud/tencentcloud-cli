**Example 1: 更新流量镜像过滤规则**

更新流量镜像过滤规则

Input: 

```
tccli vpc ResetTrafficMirrorFilter --cli-unfold-argument  \
    --TrafficMirrorId imgf-cvfp7xo8 \
    --NatId nat-qo7kugzg
```

Output: 
```
{
    "Response": {
        "RequestId": "404428db-f850-40c2-803d-0aae49aba43a"
    }
}
```

