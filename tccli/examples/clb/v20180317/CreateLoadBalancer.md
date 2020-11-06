**Example 1: Creating a public network CLB instance**

This example shows you how to create a public network CLB instance in a VPC.

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

**Example 2: Creating a private network CLB instance**

This example shows you how to create a private network CLB instance in a VPC.

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

