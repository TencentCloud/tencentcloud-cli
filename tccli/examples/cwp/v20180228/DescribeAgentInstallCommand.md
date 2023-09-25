**Example 1: DescribeAgentInstallCommand**



Input: 

```
tccli cwp DescribeAgentInstallCommand --cli-unfold-argument  \
    --ExpireDate 2020-09-22 \
    --RegionCode xx \
    --VpcId xx \
    --IsCloud True \
    --NetType xx \
    --TagIds 1
```

Output: 
```
{
    "Response": {
        "WindowsCommand": "xx",
        "LinuxCommand": "xx",
        "ARMCommand": "xx",
        "WindowsDownloadUrl": "xx",
        "RequestId": "xx",
        "WindowsStepOne": "xx",
        "WindowsStepTwo": "xx"
    }
}
```

