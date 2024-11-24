**Example 1: 重置流量镜像采集对象**



Input: 

```
tccli vpc ResetTrafficMirrorSrcs --cli-unfold-argument  \
    --TrafficMirrorId imgf-cvfp7xo8 \
    --CollectorSrcs subnet-q304e5h2 subnet-7v7ev09m
```

Output: 
```
{
    "Response": {
        "RequestId": "404428db-f850-40c2-803d-0aae49aba43a"
    }
}
```

