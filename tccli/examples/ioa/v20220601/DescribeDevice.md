**Example 1: test**

123

Input: 

```
tccli ioa DescribeDevice --cli-unfold-argument  \
    --Mid abc
```

Output: 
```
{
    "Response": {
        "Data": {
            "Id": 0,
            "Mid": "abc",
            "Name": "abc",
            "GroupId": 0,
            "OsType": 0,
            "Ip": "abc",
            "OnlineStatus": 0,
            "Version": "abc",
            "StrVersion": "abc",
            "Itime": "abc",
            "ConnActiveTime": "abc",
            "Locked": 0,
            "LocalIpList": "abc",
            "HostId": 0,
            "GroupName": "abc",
            "GroupNamePath": "abc",
            "CriticalVulListCount": 0,
            "Os": "abc",
            "OsBits": 0,
            "OsVersion": "abc",
            "OsLanguage": "abc",
            "OsInstallDate": "abc",
            "ComputerName": "abc",
            "DomainName": "abc",
            "MacAddr": "abc",
            "VulCount": 0,
            "RiskCount": 0,
            "VirusVer": "abc",
            "VulVersion": "abc",
            "SysRepVersion": "abc",
            "VulCriticalList": [
                "abc"
            ],
            "Tags": "abc",
            "UserName": "abc",
            "FirewallStatus": 0,
            "SerialNum": "abc",
            "DeviceStrategyVer": "abc",
            "NGNStrategyVer": "abc",
            "IOAUserName": "abc",
            "DeviceNewStrategyVer": "abc",
            "NGNNewStrategyVer": "abc",
            "HostName": "abc",
            "BaseBoardSn": "abc",
            "AccountUsers": "abc",
            "IdentityStrategyVer": "abc",
            "IdentityNewStrategyVer": "abc",
            "AccountGroupName": "abc",
            "AccountName": "abc",
            "AccountGroupId": 0
        },
        "RequestId": "abc"
    }
}
```

**Example 2: 测试**

测试

Input: 

```
tccli ioa DescribeDevice --cli-unfold-argument  \
    --Mid EBCDB9C9923516F3C02B42B42DA564E7653F6EBC02
```

Output: 
```
{
    "Response": {
        "Data": {
            "AccountGroupId": 0,
            "AccountGroupName": "",
            "AccountName": "",
            "AccountUsers": "未绑定",
            "BaseBoardSn": "",
            "ComputerName": "YF的Mac (2)",
            "ConnActiveTime": "2023-11-24T16:54:01.797491+08:00",
            "CriticalVulListCount": 0,
            "DeviceNewStrategyVer": "",
            "DeviceStrategyVer": "",
            "DiskAccessPermission": 0,
            "DomainName": "",
            "FirewallStatus": 0,
            "GroupId": 99,
            "GroupName": "未分组终端",
            "GroupNamePath": "全网终端.未分组终端",
            "HostId": 0,
            "HostName": "",
            "IOAUserName": "",
            "Id": 42,
            "IdentityNewStrategyVer": "",
            "IdentityStrategyVer": "",
            "Ip": "14.22.11.171",
            "Itime": "2023-10-30T16:52:12.748539+08:00",
            "LocalIpList": "10.211.55.9",
            "Locked": 0,
            "MacAddr": "00:1C:42:C1:08:CD",
            "Mid": "EBCDB9C9923516F3C02B42B42DA564E7653F6EBC02",
            "NGNNewStrategyVer": "",
            "NGNStrategyVer": "",
            "Name": "YF的Mac (2)",
            "OnlineStatus": 1,
            "Os": "macOS 12.5 (21G72)",
            "OsBits": 64,
            "OsInstallDate": "",
            "OsLanguage": "",
            "OsType": 2,
            "OsVersion": "版本12.5（版号21G72）",
            "RiskCount": 0,
            "ScreenRecordingPermission": 0,
            "SerialNum": "",
            "StrVersion": "208.13.112.1222",
            "SysRepVersion": "",
            "Tags": "",
            "UserName": "yfchen",
            "Version": "58546850997732550",
            "VirusVer": "2.0.560.63",
            "VulCount": 0,
            "VulCriticalList": [],
            "VulVersion": ""
        },
        "RequestId": "d097d971-a4e9-4098-a19a-3231f5f4b6eb"
    }
}
```

