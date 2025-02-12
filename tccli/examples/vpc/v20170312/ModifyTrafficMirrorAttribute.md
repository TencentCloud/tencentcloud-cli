**Example 1: 修改流量镜像属性**

修改流量镜像属性

Input: 

```
tccli vpc ModifyTrafficMirrorAttribute --cli-unfold-argument  \
    --TrafficMirrorId imgf-7h62jza4 \
    --TrafficMirrorName test \
    --TrafficMirrorDescription test_info
```

Output: 
```
{
    "Response": {
        "RequestId": "404428db-f850-40c2-803d-0aae49aba43a"
    }
}
```

