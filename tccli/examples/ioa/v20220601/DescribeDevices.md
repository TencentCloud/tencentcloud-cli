**Example 1: 获取设备列表详情**

获取租户满足条件：最近登录账号包含\'cc\'（不区分大小写）的设备列表详情

Input: 

```
tccli ioa DescribeDevices --cli-unfold-argument  \
    --Condition.FilterGroups.0.Filters.0.Field IOAUserName \
    --Condition.FilterGroups.0.Filters.0.Operator ilike \
    --Condition.FilterGroups.0.Filters.0.Values cc \
    --Condition.PageSize 10 \
    --Condition.PageNum 1 \
    --GroupId 93 \
    --OsType 0
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "AccountGroupId": 298,
                    "AccountGroupName": "cc",
                    "AccountName": "cc",
                    "AccountUsers": "cc",
                    "BaseBoardSn": "N0CV1740MB0020008",
                    "ComputerName": "DESKTOP-AL8RU6H",
                    "ConnActiveTime": "2023-12-01T12:11:47.076416+08:00",
                    "CriticalVulListCount": 0,
                    "DeviceNewStrategyVer": "2023-12-01 12:11:00",
                    "DeviceStrategyVer": "2023-12-01 11:10:00",
                    "DomainName": "obsolete",
                    "FirewallStatus": 1,
                    "GroupId": 93,
                    "GroupName": "未分组终端",
                    "GroupNamePath": "全网终端.未分组终端",
                    "HostId": 0,
                    "HostName": "obsolete",
                    "IOAUserName": "cc",
                    "Id": 54,
                    "IdentityNewStrategyVer": "2024-11-06 02:44:00",
                    "IdentityStrategyVer": "2024-10-24 22:33:00",
                    "Ip": "113.108.77.51",
                    "Itime": "2023-12-01T09:37:38.505458+08:00",
                    "LocalIpList": "192.168.0.128",
                    "Locked": 0,
                    "MacAddr": "00:0C:29:10:00:5C",
                    "Mid": "75129D715480905B6A9C4569893C7634656938E2",
                    "NGNNewStrategyVer": "2023-11-20 15:54:00",
                    "NGNStrategyVer": "2023-11-20 15:54:00",
                    "Name": "DESKTOP-AL8RU6H",
                    "OnlineStatus": 1,
                    "Os": "Microsoft Windows 10 专业版",
                    "OsBits": 64,
                    "OsInstallDate": "20220812112555.000000+480",
                    "OsLanguage": "简体中文",
                    "OsType": 0,
                    "OsVersion": "10.0.19045",
                    "RiskCount": 0,
                    "SerialNum": "VMware-56 4d 76 2d d7 24 e1 ab-43 f3 af 25 e3 10 00 5c",
                    "StrVersion": "209.12.18590.201",
                    "SysRepVersion": "2023.11.30.19.52.38",
                    "Tags": "commpany assert",
                    "UserName": "cc",
                    "Version": "58828322890449097",
                    "VirusVer": "2.0.13712.288",
                    "VulCount": 0,
                    "VulCriticalList": [
                        "5043051",
                        "4132216"
                    ],
                    "VulVersion": "2023.11.21.16.28.52"
                }
            ],
            "Paging": {
                "PageCount": 1,
                "PageNum": 1,
                "PageSize": 10,
                "Total": 1
            }
        },
        "RequestId": "807938c5-9308-4c87-918d-e84a05f226a1"
    }
}
```

