**Example 1: 接口测试**

接口测试

Input: 

```
tccli csip DescribeCVMAssetInfo --cli-unfold-argument  \
    --AssetId ins-ggrnxdwj
```

Output: 
```
{
    "Response": {
        "Data": {
            "VpcId": "vpc-pr0wcl5e",
            "VpcName": "fengqqian",
            "AssetName": "主机测试2-win",
            "Os": "Windows Server 2012 R2 数据中心版 64位中文版",
            "PublicIp": "139.155.142.171",
            "PrivateIp": "172.16.0.9",
            "Region": "ap-chengdu",
            "AssetType": "CVM",
            "AssetId": "ins-ggrnxdwj",
            "AccountNum": 2,
            "PortNum": 19,
            "ProcessNum": 41,
            "SoftApplicationNum": 1,
            "DatabaseNum": 0,
            "WebApplicationNum": 0,
            "ServiceNum": 0,
            "WebFrameworkNum": 0,
            "WebSiteNum": 0,
            "JarPackageNum": 0,
            "StartServiceNum": 173,
            "ScheduledTaskNum": 91,
            "EnvironmentVariableNum": 0,
            "KernelModuleNum": 0,
            "SystemInstallationPackageNum": 0,
            "SurplusProtectDay": 33,
            "CWPStatus": 4,
            "Tag": [
                {
                    "Name": "name1",
                    "Value": "value1"
                }
            ],
            "ProtectLevel": "旗舰版",
            "ProtectedDay": 2
        },
        "RequestId": "8c9f9ac1-73a5-4241-b314-871b8623b017"
    }
}
```

