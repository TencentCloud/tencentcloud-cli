**Example 1: 解绑一个传统型负载均衡的后端服务**



Input: 

```
tccli clb DeregisterTargetsFromClassicalLB --cli-unfold-argument  \
    --LoadBalancerId lb-a3u5l5zc \
    --InstanceIds ins-odjhn6vc
```

Output: 
```
{
    "Response": {
        "RequestId": "a8ae0a06-f935-4a1b-bc73-f5055f3e1954"
    }
}
```

