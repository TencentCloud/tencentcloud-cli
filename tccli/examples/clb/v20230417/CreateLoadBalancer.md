**Example 1: 创建一个公网负载均衡实例**

在私有网络中创建一个公网负载均衡

Input: 

```
tccli clb CreateLoadBalancer --cli-unfold-argument  \
    --Forward 1 \
    --ProjectId 0 \
    --LoadBalancerType OPEN \
    --VpcId vpc-30xqxt9p \
    --LoadBalancerName test
```

Output: 
```
{
    "Response": {
        "LoadBalancerIds": [
            "lb-6efswuxa"
        ],
        "DealName": "20220101660009831340631",
        "RequestId": "9b3f0b57-fb64-4918-8dd6-ce02604fb52c"
    }
}
```

**Example 2: 创建一个内网负载均衡实例**

在私有网络中创建一个内网负载均衡

Input: 

```
tccli clb CreateLoadBalancer --cli-unfold-argument  \
    --Forward 1 \
    --SubnetId subnet-k57djpow \
    --LoadBalancerType INTERNAL \
    --VpcId vpc-30xqxt9p \
    --LoadBalancerName test_internal
```

Output: 
```
{
    "Response": {
        "LoadBalancerIds": [
            "lb-kmfrnqci"
        ],
        "DealName": "20211230660009761735781",
        "RequestId": "7ffa6830-cd1b-4bc4-8e24-1688885f594a"
    }
}
```

