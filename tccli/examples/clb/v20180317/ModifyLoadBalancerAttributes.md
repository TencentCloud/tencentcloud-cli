**Example 1: Renaming a CLB instance**



Input: 

```
tccli clb ModifyLoadBalancerAttributes --cli-unfold-argument  \
    --LoadBalancerId lb-6efswuxa\
    --LoadBalancerName newlbname
```

Output: 
```
{
    "Response": {
        "RequestId": "78a40898-8210-44c7-8bc6-f83e50878d12"
    }
}
```

**Example 2: Setting the cross-region attribute of a CLB instance**



Input: 

```
tccli clb ModifyLoadBalancerAttributes --cli-unfold-argument  \
    --LoadBalancerId lb-6efswuxa\
    --TargetRegionInfo.Region ap-shanghai\
    --TargetRegionInfo.VpcId vpc-abcd1234
```

Output: 
```
{
    "Response": {
        "DealName": null,
        "RequestId": "78a40898-8210-44c7-8bc6-f83e5087ad54"
    }
}
```

