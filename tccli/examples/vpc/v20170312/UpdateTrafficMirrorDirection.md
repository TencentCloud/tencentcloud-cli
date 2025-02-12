**Example 1: 更改流量镜像采集方向**

更改流量镜像采集方向

Input: 

```
tccli vpc UpdateTrafficMirrorDirection --cli-unfold-argument  \
    --TrafficMirrorId imgf-cvfp7xo8 \
    --Direction INGRESS
```

Output: 
```
{
    "Response": {
        "RequestId": "404428db-f850-40c2-803d-0aae49aba43a"
    }
}
```

