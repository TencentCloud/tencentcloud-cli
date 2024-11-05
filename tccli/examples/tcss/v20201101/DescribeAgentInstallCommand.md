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
        "ARMCommand": "wget http://a.com/ydeyes_linux64_aarch64.tar.gz -O ydeyes_linux64_aarch64.tar.gz && tar -zxvf ydeyes_linux64_aarch64.tar.gz && ./self_cloud_install_linux64.sh",
        "LinuxCommand": "wget http://a.comydeyes_linux64.tar.gz -O ydeyes_linux64.tar.gz && tar -zxvf ydeyes_linux64.tar.gz && ./self_cloud_install_linux64.sh",
        "RequestId": "751c2a46-7ef4-4932-ac06-5ccc2faa74fb",
        "WindowsCommand": "powershell -executionpolicy bypass -c \"(New-Object Net.WebClient).DownloadFile('http://a.com/ydeyes_win32.exe', $ExecutionContext.SessionState.Path.GetUnresolvedProviderPathFromPSPath('.\\ydeyes_win32.exe'))\"; \"./ydeyes_win32.exe\"",
        "WindowsDownloadUrl": "https://a.com/ydeyes_win32.exe",
        "WindowsStepOne": "http://a.com/ydeyes_win32.exe",
        "WindowsStepTwo": "ydeyes_win32.exe"
    }
}
```

