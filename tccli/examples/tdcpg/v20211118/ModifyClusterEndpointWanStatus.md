**Example 1: 修改接入点外网状态**



Input: 

```
tccli tdcpg ModifyClusterEndpointWanStatus --cli-unfold-argument  \
    --ClusterId tdcpg-xxx \
    --EndpointId tdcpg-ep-xxx \
    --WanStatus OPEN
```

Output: 
```
{
    "Response": {
        "RequestId": "03ea3f94-297d-11eb-8f30-525400b7dd5a"
    }
}
```

