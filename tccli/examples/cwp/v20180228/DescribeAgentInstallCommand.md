**Example 1: DescribeAgentInstallCommand**



Input: 

```
tccli cwp DescribeAgentInstallCommand --cli-unfold-argument  \
    --ExpireDate 2020-09-22 \
    --RegionCode gz \
    --VpcId vpc-12345 \
    --IsCloud True \
    --NetType public \
    --TagIds 1
```

Output: 
```
{
    "Response": {
        "WindowsCommand": "ydeyes.exe",
        "LinuxCommand": "ydeyes.exe",
        "ARMCommand": "ydeyes.exe",
        "WindowsDownloadUrl": "ydeyes.exe",
        "RequestId": "1234-1234-1234",
        "WindowsStepOne": "ydeyes.exe",
        "WindowsStepTwo": "ydeyes.exe"
    }
}
```

