**Example 1: 评估用户风险质量**



Input: 

```
tccli trdp EvaluateUserRisk --cli-unfold-argument  \
    --Account.UniversalAccount.AccountId xx \
    --Account.AccountType 1 \
    --Marketing.FullScreen 0 \
    --Marketing.AdvertisingSpaceWidth 0 \
    --Marketing.Url xx \
    --Marketing.AdvertisingSpaceHeight 0 \
    --Marketing.AdvertisingType 1 \
    --Marketing.DeliveryMode 1 \
    --DeviceDetail.Lon xx \
    --DeviceDetail.Lat xx \
    --DeviceDetail.PackageName xx \
    --DeviceDetail.SerialNumber xx \
    --DeviceDetail.Storage xx \
    --DeviceDetail.Memory xx \
    --DeviceDetail.ChargeStatus xx \
    --DeviceDetail.DeviceVersion xx \
    --DeviceDetail.DeviceName xx \
    --DeviceDetail.CpuModel xx \
    --DeviceDetail.BluetoothAddress xx \
    --DeviceDetail.AppName xx \
    --DeviceDetail.AppPackageName xx \
    --DeviceDetail.OsSystem xx \
    --DeviceDetail.MobileCountryAndNetworkCode xx \
    --DeviceDetail.Volume xx \
    --DeviceDetail.ResolutionWidth 0 \
    --DeviceDetail.CpuCore xx \
    --DeviceDetail.IsProxy xx \
    --DeviceDetail.BidFloor 0 \
    --DeviceDetail.Language xx \
    --DeviceDetail.MacAddress xx \
    --DeviceDetail.AccessMode xx \
    --DeviceDetail.ResolutionHeight 0 \
    --DeviceDetail.AppVersion xx \
    --DeviceDetail.OsSystemVersion xx \
    --DeviceDetail.Carrier xx \
    --DeviceDetail.DeviceType xx \
    --DeviceDetail.BatteryPower xx \
    --DeviceDetail.Model xx \
    --DeviceDetail.Ua xx \
    --DeviceDetail.Maker xx \
    --DeviceDetail.KernelVersion xx \
    --DeviceDetail.BaseBandVersion xx \
    --DeviceDetail.StartupTime xx \
    --DeviceDetail.IsRoot xx \
    --DeviceDetail.WifiMac xx \
    --DeviceDetail.AndroidApiLevel xx \
    --DeviceDetail.App xx \
    --DeviceDetail.Brightness xx \
    --DeviceDetail.IsDebug xx \
    --DeviceDetail.VendorId xx \
    --DeviceDetail.NetworkType xx \
    --DeviceDetail.IsEmulator xx \
    --DeviceDetail.PhoneChipInfo xx \
    --User.Name xx \
    --User.Ip xx \
    --User.Age 0 \
    --User.ChannelSource xx \
    --User.ResidentIdentityCard xx \
    --User.Platform 1 \
    --User.Gender xx \
    --User.Address xx \
    --User.Nickname xx \
    --User.Email xx \
    --SceneCode xx \
    --DeviceFingerprint.DeviceToken xx \
    --DeviceFingerprint.SdkChannel xx \
    --ModelId xx
```

Output: 
```
{
    "Response": {
        "RequestId": "xxxxxxxxxxxxxxxxxx",
        "EvaluationResult": {
            "RiskLabels": [
                201,
                205
            ],
            "Score": 43.1,
            "SSID": "xxxxxxxxxxxxx"
        }
    }
}
```

