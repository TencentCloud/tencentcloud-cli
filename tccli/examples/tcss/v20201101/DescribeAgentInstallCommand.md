**Example 1: 查询agent安装命令**



Input: 

```
tccli tcss DescribeAgentInstallCommand --cli-unfold-argument  \
    --IsCloud true \
    --NetType "basic"
```

Output: 
```
{
    "Response": {
        "WindowsCommand": "xx",
        "LinuxCommand": "xx",
        "WindowsDownloadUrl": "xx",
        "RequestId": "xx",
        "WindowsStepOne": "xx",
        "WindowsStepTwo": "xx"
    }
}
```

