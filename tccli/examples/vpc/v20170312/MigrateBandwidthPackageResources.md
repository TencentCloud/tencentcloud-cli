**Example 1: 资源在精品带宽包之间迁移**

资源在精品带宽包之间迁移。

Input: 

```
tccli vpc MigrateBandwidthPackageResources --cli-unfold-argument  \
    --BandwidthPackageId bwp-hxlqja90 \
    --TargetBandwidthPackageId bwp-hxlqja90 \
    --ResourceIds eip-hxlqja90 eip-hxlqja91
```

Output: 
```
{
    "Response": {
        "RequestId": "42bc5893-70ff-4f13-bcc3-1308dedab8f6"
    }
}
```

