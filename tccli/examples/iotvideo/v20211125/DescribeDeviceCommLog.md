**Example 1: 获取设备通讯日志**



Input: 

```
tccli iotvideo DescribeDeviceCommLog --cli-unfold-argument  \
    --ProductId TDCZ2WD29Z \
    --DeviceName DoNotDelete_34082530_1 \
    --MinTime 1612235855834 \
    --MaxTime 1612237655834
```

Output: 
```
{
    "Response": {
        "Context": "DnF1ZXJ5VGhlbkZldGNoBQAAAAAAk0zFFnBpdzE2UUE4UlZ1UnFtTjhIeV81THcAAAAAAIJzFxZ2aThIdjFTVlJveUo3aGEzRlBrRkdRAAAAAABDhPEWaUdjOWIxWTBUQ3lWNGxVOC1CeGQ5ZwAAAAAAX2TWFl9CSDZsdnE1UkNpbmJ3U3lfNTVGX0EAAAAAAIKcmhZDTnp1RmZPNVFVR1pLMWF4Q3V5eDNR",
        "Listover": true,
        "RequestId": "ce3c2fd6-e5d2-4676-9696-3d27e52f608d",
        "Results": []
    }
}
```

