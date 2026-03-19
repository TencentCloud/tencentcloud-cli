**Example 1: 开启带宽包流量校验开关**



Input: 

```
tccli vpc ModifyBandwidthPackageAttribute --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "54c9bac3-c94d-4d2d-8104-54f0691bffdd"
    }
}
```

**Example 2: 修改带宽包名称**



Input: 

```
tccli vpc ModifyBandwidthPackageAttribute --cli-unfold-argument  \
    --BandwidthPackageId bwp-il9224p5 \
    --BandwidthPackageName demo
```

Output: 
```
{
    "Response": {
        "RequestId": "6b864a91-9ab6-4977-9641-d99bf55f6fed"
    }
}
```

