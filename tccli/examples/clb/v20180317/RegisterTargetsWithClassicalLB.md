**Example 1: 绑定一个后端服务到传统型负载均衡**



Input: 

```
tccli clb RegisterTargetsWithClassicalLB --cli-unfold-argument  \
    --LoadBalancerId lb-a3u5l5zc \
    --Targets.0.InstanceId ins-lhhn9fhk \
    --Targets.0.Weight 20
```

Output: 
```
{
    "Response": {
        "RequestId": "bab5b8c4-7e9f-4032-90fb-c61ee6678c73"
    }
}
```

