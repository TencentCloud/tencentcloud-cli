**Example 1: 诊断负载均衡的健康检查源IP**

诊断指定负载均衡的健康检查源IP是否为VIP。

Input: 

```
tccli clb CheckLBHealthSourceIP --cli-unfold-argument  \
    --LoadBalancerIds lb-jc1z46** lb-if8fml**
```

Output: 
```
{
    "Response": {
        "RequestId": "4b368eea-4e9d-469f-8a26-3164e8dd6f**"
    }
}
```

