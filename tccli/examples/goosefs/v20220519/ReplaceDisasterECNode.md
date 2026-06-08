**Example 1: 更换EC集群里面的故障节点**

用于更换EC集群中的故障节点

Input: 

```
tccli goosefs ReplaceDisasterECNode --cli-unfold-argument  \
    --FileSystemId x-c73-6s184jpn \
    --OwnerUin 3472213910 \
    --ECRecoverGroupId x_c73_6s184jpn_ec_rg_002 \
    --TargetNodeId x-c73-6s184jpn-owner-nsd-rg-002-002
```

Output: 
```
{
    "Response": {
        "RequestId": "0e49bd11-27eb-452f-9a06-e3d059cce676"
    }
}
```

