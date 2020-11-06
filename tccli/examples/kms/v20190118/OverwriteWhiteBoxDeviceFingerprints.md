**Example 1: 覆盖指定密钥的设备指纹信息**



Input: 

```
tccli kms OverwriteWhiteBoxDeviceFingerprints --cli-unfold-argument  \
    --KeyId cd850a3d-9b1b-11ea-a96a-5254006d0810 \
    --DeviceFingerprints.0.Identity c19c024c-2ba1-11b2-a85c-96f970f4a8e1 \
    --DeviceFingerprints.0.Description desc1
```

Output: 
```
{
    "Response": {
        "RequestId": "c8d1f1b9-632a-4c0b-b369-9bcf8e7e6ef9"
    }
}
```

