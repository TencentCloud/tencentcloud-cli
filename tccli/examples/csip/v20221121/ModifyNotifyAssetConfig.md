**Example 1: 示例**



Input: 

```
tccli csip ModifyNotifyAssetConfig --cli-unfold-argument  \
    --Items.0.Module Agent \
    --Items.0.SubModule  \
    --Items.0.AssetRange 1 \
    --Items.0.ExcludedInstanceIds ins-xxx
```

Output: 
```
{
    "Response": {
        "RequestId": "32a21e5b-14e2-4c89-b1ed-a65ae63fdd08"
    }
}
```

