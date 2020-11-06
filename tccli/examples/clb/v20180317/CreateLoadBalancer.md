**Example 1: 创建一个公网负载均衡实例**

在私有网络中创建一个公网负载均衡

Input: 

```
tccli clb CreateLoadBalancer --cli-unfold-argument  \
    --LoadBalancerType OPEN \
    --Forward 1 \
    --VpcId vpc-30xqxt9p \
    --LoadBalancerName test \
    --ProjectId 0
```

Output: 
```
{
    "Response": {
        "LoadBalancerIds": [
            "lb-6efswuxa"
        ],
        "RequestId": "9b3f0b57-fb64-4918-8dd6-ce02604fb52c"
    }
}
```

**Example 2: 创建一个内网负载均衡实例**

在私有网络中创建一个内网负载均衡

Input: 

```
tccli clb CreateLoadBalancer --cli-unfold-argument  \
    --LoadBalancerType INTERNAL \
    --Forward 1 \
    --LoadBalancerName test_internal \
    --VpcId vpc-30xqxt9p \
    --SubnetId subnet-k57djpow
```

Output: 
```
{
    "Response": {
        "LoadBalancerIds": [
            "lb-kmfrnqci"
        ],
        "RequestId": "7ffa6830-cd1b-4bc4-8e24-1688885f594a"
    }
}
```

