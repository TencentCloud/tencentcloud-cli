**Example 1: 非加密快照转加密快照**

非加密快照转加密快照

Input: 

```
tccli cbs CreateEncryptSnapshot --cli-unfold-argument  \
    --ExtraInfo {"ItemId": 0, "DeviceImageId": 0, "OsName": "Xserver windows2019cndatacenterx86_64", "ImageId": "img2022121404773373"} \
    --SnapshotId snap-bh2d9l10
```

Output: 
```
{
    "Response": {
        "EncryptType": "encrypt_spdk",
        "RequestId": "a0ed56a0-4b9a-4690-bd5e-7aa76fd67b4d",
        "SnapshotId": "snap-bh2d9l10"
    }
}
```

