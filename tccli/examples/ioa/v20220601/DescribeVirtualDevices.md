**Example 1: 示例1**



Input: 

```
tccli ioa DescribeVirtualDevices --cli-unfold-argument  \
    --DeviceVirtualGroupId 356 \
    --OsType 0 \
    --Condition.PageSize 10 \
    --Condition.PageNum 1
```

Output: 
```
{
    "Response": {
        "RequestId": "ce9f337a-55c4-4a44-8c0c-c32462e03da8",
        "Data": {
            "Items": [
                {
                    "FirewallStatus": 0,
                    "Locked": 0,
                    "DeviceStrategyVer": "",
                    "NGNStrategyVer": "",
                    "IOAUserName": "",
                    "DeviceNewStrategyVer": "",
                    "NGNNewStrategyVer": "2022-07-28 15:21:00",
                    "HostName": "",
                    "UserName": "niozhang",
                    "Version": "28429406901371100",
                    "Itime": "2022-10-21T15:21:37.460778+08:00",
                    "Os": "",
                    "Mid": "13fabc68a4834ba08d14afa179b7193863524881",
                    "GroupId": 42632,
                    "GroupName": "未分组终端",
                    "Ip": "106.55.201.137",
                    "OnlineStatus": 0,
                    "SerialNum": "",
                    "StrVersion": "101.101.7048.220",
                    "Tags": "",
                    "GroupNamePath": "全网终端.未分组终端",
                    "Id": 25902,
                    "ConnActiveTime": "",
                    "LocalIpList": "",
                    "HostId": 0,
                    "Name": "BindDeviceTest1666336897217",
                    "OsType": 0,
                    "CriticalVulListCount": 0,
                    "OsBits": 0,
                    "OsVersion": "",
                    "OsLanguage": "",
                    "OsInstallDate": "",
                    "ComputerName": "BindDeviceTest1666336897217",
                    "DomainName": "",
                    "MacAddr": "",
                    "VulCount": 0,
                    "RiskCount": 0,
                    "VirusVer": "",
                    "VulVersion": "",
                    "SysRepVersion": "",
                    "VulCriticalList": []
                }
            ],
            "Paging": {
                "PageNum": 1,
                "Total": 1,
                "PageCount": 1,
                "PageSize": 10
            }
        }
    }
}
```

