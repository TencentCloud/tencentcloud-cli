**Example 1: Getting the device fingerprint list of a specified key**



Input: 

```
tccli kms DescribeWhiteBoxDeviceFingerprints --cli-unfold-argument  \
    --KeyId cd850a3d-9b1b-11ea-a96a-5254006d0810
```

Output: 
```
{
    "Response": {
        "RequestId": "f643be96-3ea8-4abe-b148-0cc74436b2c1",
        "DeviceFingerprints": [
            {
                "Identity": "c19c024c-2ba1-11b2-a85c-96f970f4a8e1",
                "Description": "desc"
            }
        ]
    }
}
```

