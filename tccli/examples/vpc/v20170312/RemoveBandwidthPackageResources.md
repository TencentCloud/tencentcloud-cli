**Example 1: 带宽包内资源移除**



Input: 

```
tccli vpc RemoveBandwidthPackageResources --cli-unfold-argument  \
    --BandwidthPackageId bwp-sddefxdf \
    --ResourceType Address \
    --ResourceIds eip-wekidufh eip-djthcjrv
```

Output: 
```
{
    "Response": {
        "RequestId": "0a82e871-6574-429e-8506-1cce14aac843"
    }
}
```

