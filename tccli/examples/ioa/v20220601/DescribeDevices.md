**Example 1: 根据最近登录账号获取设备列表详情**

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
                    "Profiles": [
                        {
                            "Mid": "75129D715480905B6A9C4569893C7634656938E2",
                            "IsCustom": "obsolete",
                            "IsMust": "1",
                            "Type": 4,
                            "FieldId": 166,
                            "Value": "Private assets",
                            "Title": "Company assets",
                            "Options": "obsolete"
                        }
                    ],
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

**Example 2: 根据终端信息登记电话查找终端列表数据**

根据终端信息登记电话查找终端列表数据

Input: 

```
tccli ioa DescribeDevices --cli-unfold-argument  \
    --Condition.FilterGroups.0.Filters.0.Field profile_1477202 \
    --Condition.FilterGroups.0.Filters.0.Operator eq \
    --Condition.FilterGroups.0.Filters.0.Values 158****3237 177****2517 \
    --Condition.PageNum 1 \
    --Condition.PageSize 10 \
    --GroupId 1652026 \
    --OsType -1 \
    --PageNum 1 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "AccountGroupId": 0,
                    "AccountGroupName": "",
                    "AccountName": "",
                    "AccountUsers": "",
                    "BaseBoardSn": "",
                    "BiosUuid": "",
                    "ComputerName": "DESKTOP-TJU79MK",
                    "ConnActiveTime": "2026-08-07T18:41:56.353633+08:00",
                    "CriticalVulListCount": 2,
                    "DeviceNewStrategyVer": "2026-09-21 19:00:00",
                    "DeviceStrategyVer": "2026-08-07 17:49:00",
                    "DiskAccessPermission": 0,
                    "DomainName": "",
                    "FirewallStatus": 0,
                    "GroupId": 1652027,
                    "GroupName": "未分组终端",
                    "GroupNamePath": "全网终端.未分组终端",
                    "HostId": 0,
                    "HostName": "",
                    "IOAUserName": "",
                    "Id": 2010536,
                    "IdentityNewStrategyVer": "",
                    "IdentityStrategyVer": "",
                    "InstallationStatus": 0,
                    "Ip": "113.108.77.60",
                    "Itime": "2026-08-07T17:44:18.619623+08:00",
                    "LocalIpList": "192.168.21.129",
                    "Locked": 0,
                    "MacAddr": "00:0C:29:A9:79:C4",
                    "Mid": "44F3EFD79E9CB55BEA5A100CF67C0BDD6A75A8F2",
                    "NGNNewStrategyVer": "2026-08-06 17:05:00",
                    "NGNStrategyVer": "",
                    "Name": "DESKTOP-TJU79MK",
                    "OnlineStatus": 1,
                    "Os": "Microsoft Windows 10 专业版",
                    "OsBits": 64,
                    "OsInstallDate": "20250423100243.000000+480",
                    "OsLanguage": "简体中文",
                    "OsType": 0,
                    "OsVersion": "10.0.19045",
                    "Profiles": [
                        {
                            "FieldId": 1477202,
                            "IsCustom": "",
                            "IsMust": "1",
                            "Mid": "44F3EFD79E9CB55BEA5A100CF67C0BDD6A75A8F2",
                            "Options": "**",
                            "Title": "电话",
                            "Type": 1,
                            "Value": "177****2517"
                        }
                    ],
                    "RemarkName": "",
                    "RiskCount": 0,
                    "ScreenRecordingPermission": 0,
                    "SerialNum": "VMware-56 4d 13 1c 33 1d aa 9c-91 c0 ca 6e f3 a9 79 c4",
                    "StrVersion": "211.7.33303.62001",
                    "SysRepVersion": "2025.09.09.18.20.25",
                    "Tags": "",
                    "UserName": "xsc",
                    "Version": "59391252333326897",
                    "VirusVer": "2.0.13789.1131",
                    "VulCount": 0,
                    "VulCriticalList": [],
                    "VulVersion": "2026.08.05.10.15.05"
                },
                {
                    "AccountGroupId": 0,
                    "AccountGroupName": "",
                    "AccountName": "",
                    "AccountUsers": "",
                    "BaseBoardSn": "",
                    "BiosUuid": "",
                    "ComputerName": "lucal_win-PC",
                    "ConnActiveTime": "2026-08-07T03:00:00.003214+08:00",
                    "CriticalVulListCount": 0,
                    "DeviceNewStrategyVer": "2026-09-21 19:00:00",
                    "DeviceStrategyVer": "",
                    "DiskAccessPermission": 0,
                    "DomainName": "",
                    "FirewallStatus": 0,
                    "GroupId": 1652027,
                    "GroupName": "未分组终端",
                    "GroupNamePath": "全网终端.未分组终端",
                    "HostId": 0,
                    "HostName": "",
                    "IOAUserName": "",
                    "Id": 2009787,
                    "IdentityNewStrategyVer": "",
                    "IdentityStrategyVer": "",
                    "InstallationStatus": 0,
                    "Ip": "119.147.10.194",
                    "Itime": "2026-08-06T17:09:24.795024+08:00",
                    "LocalIpList": "192.168.202.1,192.168.0.1",
                    "Locked": 0,
                    "MacAddr": "",
                    "Mid": "7EBWA5184BEC838B96B29CE8105EC6616A744F44",
                    "NGNNewStrategyVer": "2026-08-06 17:05:00",
                    "NGNStrategyVer": "",
                    "Name": "lucal_win-PC",
                    "OnlineStatus": 0,
                    "Os": "",
                    "OsBits": 0,
                    "OsInstallDate": "",
                    "OsLanguage": "",
                    "OsType": 0,
                    "OsVersion": "",
                    "Profiles": [
                        {
                            "FieldId": 1477202,
                            "IsCustom": "",
                            "IsMust": "1",
                            "Mid": "7EBWA5184BEC838B96B29CE8105EC6616A744F44",
                            "Options": "***",
                            "Title": "电话",
                            "Type": 1,
                            "Value": "158****3237"
                        }
                    ],
                    "RemarkName": "",
                    "RiskCount": 0,
                    "ScreenRecordingPermission": 0,
                    "SerialNum": "",
                    "StrVersion": "0.0.0.0",
                    "SysRepVersion": "",
                    "Tags": "",
                    "UserName": "lucal_win-pc1",
                    "Version": "0",
                    "VirusVer": "",
                    "VulCount": 0,
                    "VulCriticalList": [],
                    "VulVersion": ""
                }
            ],
            "Paging": {
                "PageCount": 1,
                "PageNum": 1,
                "PageSize": 10,
                "Total": 2
            }
        },
        "RequestId": "4849606c-d1e6-4379-816a-55ac5a8771a0"
    }
}
```

