**Example 1: 带宽包内新增资源**



Input: 

```
tccli vpc AddBandwidthPackageResources --cli-unfold-argument  \
    --BandwidthPackageId bwp-pz5ytxu5 \
    --ResourceIds eip-gbpfd2vb \
    --ResourceType Address \
    --NetworkType BGP \
    --Protocol ipv4
```

Output: 
```
{
    "Response": {
        "RequestId": "0a82e871-6574-429e-8506-1cce14aac843"
    }
}
```

