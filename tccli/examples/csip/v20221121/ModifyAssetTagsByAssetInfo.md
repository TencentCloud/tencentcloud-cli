**Example 1: 通过资产信息操作资产绑定标签**



Input: 

```
tccli csip ModifyAssetTagsByAssetInfo --cli-unfold-argument  \
    --MemberId mem-6w**1*3 \
    --Assets.0.AppID 260096511 \
    --Assets.0.InstanceID ins-j**cms*y \
    --Assets.0.Provider t*ncent \
    --Assets.0.AssetType cvm_i*st*n*e \
    --TagIDs 11 \
    --OperationType add
```

Output: 
```
{
    "Response": {
        "Code": "0",
        "Message": "Asset tags added successfully",
        "RequestId": "fef7abee-03e9-42aa-a00b-3e07dfdabd3e"
    }
}
```

