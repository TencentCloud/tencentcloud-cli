**Example 1: 获取指定密钥的设备指纹列表**



Input: 

```
tccli kms DescribeWhiteBoxDeviceFingerprints --cli-unfold-argument  \
    --KeyId 5551ef2e-6742-11ef-8133-525400b2f623
```

Output: 
```
{
    "Response": {
        "DeviceFingerprints": [
            {
                "Description": "test1",
                "Identity": "0177ebba-5ad6930a52d808***03-ddfd218bab945f-0c275b7f7d2c8c68"
            }
        ],
        "RequestId": "5dc1c93f-8864-4525-a896-f56019aae02b"
    }
}
```

