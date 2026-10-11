**Example 1: 升级到通用 II 型实例类型**



Input: 

```
tccli redis UpgradeInstanceProductVersion --cli-unfold-argument  \
    --TargetProductVersion localv2 \
    --SwitchOption 2 \
    --InstanceId crs-3au1tc75
```

Output: 
```
{
    "Response": {
        "DealName": "20260810296023340158681",
        "RequestId": "e3802a91-5ff8-48a9-aaba-5ba42371ce02"
    }
}
```

