**Example 1: 绑定RASP授权**



Input: 

```
tccli csip ModifyCSIPRaspLicenseBinds --cli-unfold-argument  \
    --ResourceId csip-****-res-*** \
    --LicenseType RASP \
    --AssetType host \
    --InstanceIDs ins-78ip**** \
    --IsAll False
```

Output: 
```
{
    "Response": {
        "TaskId": 7527,
        "RequestId": "ef316618-7588-4db9-b951-9ec75bd79d34"
    }
}
```

