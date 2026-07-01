**Example 1: 示例**



Input: 

```
tccli csip ModifyNotifySettingAlert --cli-unfold-argument  \
    --Settings.0.Module Alert \
    --Settings.0.Mode 1 \
    --Settings.0.Status 1 \
    --Settings.0.BeginTime 00:00:00 \
    --Settings.0.EndTime 23:59:59 \
    --Settings.0.AssetRange 1 \
    --Settings.0.Option HIGH \
    --Settings.0.SubModule MALWARE_FILE
```

Output: 
```
{
    "Response": {
        "RequestId": "a87258c5-0d2c-47a9-aaad-a32de4f69f43"
    }
}
```

