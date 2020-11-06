**Example 1: 设备固件升级**



Input: 

```
tccli iotvideo UpgradeDevice --cli-unfold-argument  \
    --Tid ********* \
    --OtaVersion 1.0.1 \
    --UpgradeNow true
```

Output: 
```
{
    "Response": {
        "RequestId": "9f3c9482-c49e-431b-89e7-4ef1c1905aae",
        "Data": "{\"err_code\":0}"
    }
}
```

