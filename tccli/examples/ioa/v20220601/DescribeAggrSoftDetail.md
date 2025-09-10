**Example 1: 1**

1

Input: 

```
tccli ioa DescribeAggrSoftDetail --cli-unfold-argument  \
    --Name 1 \
    --OsType 0
```

Output: 
```
{
    "Response": {
        "Data": {
            "Name": "1",
            "OsType": 0,
            "PiracyRisk": 0,
            "Corp": "1",
            "SoftVersionDist": [
                {
                    "Version": "1",
                    "Num": 0
                }
            ],
            "PiracyVersionDist": [
                {
                    "Version": "1",
                    "Num": 0
                }
            ],
            "InstalledDeviceNum": 0,
            "PiracyInstalledDeviceNum": 0,
            "InstalledUserNum": 0,
            "PiracyInstalledUserNum": 0,
            "AuthNum": 0,
            "GenuineRate": 0
        },
        "RequestId": "1"
    }
}
```

