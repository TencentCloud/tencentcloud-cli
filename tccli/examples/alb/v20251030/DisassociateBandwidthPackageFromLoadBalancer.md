**Example 1: 实例解绑共享带宽包**



Input: 

```
tccli alb DisassociateBandwidthPackageFromLoadBalancer --cli-unfold-argument  \
    --LoadBalancerId alb-f8q2xk9m \
    --BandwidthPackageId bwp-q8m2x4pa
```

Output: 
```
{
    "Response": {
        "RequestId": "c318a537-9bfa-40c2-b6d5-e6f872ad4b1f"
    }
}
```

