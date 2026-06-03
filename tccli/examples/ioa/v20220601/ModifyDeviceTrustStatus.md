**Example 1: 将设备禁用NGN访问**



Input: 

```
tccli ioa ModifyDeviceTrustStatus --cli-unfold-argument  \
    --Status 1 \
    --DeviceIDList 9AD917AB73CBEC5FEF0B1877414C0208693683FA \
    --BlackStatusDeadline 1000000 \
    --UpdateFlags 0
```

Output: 
```
{
    "Response": {
        "RequestId": "e5c06a80-7e52-4fb7-81e6-3dbbbfde98f7"
    }
}
```

