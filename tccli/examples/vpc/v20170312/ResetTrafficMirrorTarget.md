**Example 1: 更新流量镜像接收目的信息**



Input: 

```
tccli vpc ResetTrafficMirrorTarget --cli-unfold-argument  \
    --TrafficMirrorId imgf-cvfp7xo8 \
    --CollectorTarget.TargetIps 172.16.0.3 \
    --CollectorTarget.AlgHash FIVE_TUPLE_FLOW
```

Output: 
```
{
    "Response": {
        "RequestId": "404428db-f850-40c2-803d-0aae49aba43a"
    }
}
```

