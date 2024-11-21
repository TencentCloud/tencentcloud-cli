**Example 1: 调整共享带宽包带宽**

调整共享带宽包带宽。

Input: 

```
tccli vpc ModifyBandwidthPackageBandwidth --cli-unfold-argument  \
    --InternetMaxBandwidth 100 \
    --BandwidthPackageIds bwp-alfxy9c8 \
    --BandwidthPackageId bwp-mwoqajk2
```

Output: 
```
{
    "Response": {
        "RequestId": "24cfceab-3492-482c-b86f-27f598b1b044"
    }
}
```

