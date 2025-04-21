**Example 1: 示例1**



Input: 

```
tccli ioa DescribeViruses --cli-unfold-argument  \
    --OsType 0 \
    --OnlineStatus 1 \
    --RiskStatus 1 \
    --GroupId 392
```

Output: 
```
{
    "Response": {
        "RequestId": "0518458f-4982-46a0-9a8b-6bc64485bcd6",
        "Data": {
            "Paging": {
                "PageSize": 0,
                "PageNum": 0,
                "PageCount": 0,
                "Total": 0
            },
            "Items": [
                {
                    "LocalIpList": "",
                    "Name": "",
                    "GroupFromAuto": 0,
                    "Status": 4,
                    "Desktop": 0,
                    "UDisk": 0,
                    "Download": 0,
                    "SysFile": 0,
                    "Reg": 0,
                    "Proc": 0,
                    "Driver": 0,
                    "Mid": "10db7225391fa19bade67e4bb3525c9f6376F0BE",
                    "OsBits": 0,
                    "OsVersion": "",
                    "MacAddr": "",
                    "RiskCount": 0,
                    "VirusVer": "",
                    "SysRepVersion": "",
                    "GroupNamePath": "全网终端.未分组终端",
                    "UserName": "",
                    "GroupId": 393,
                    "GroupName": "未分组终端",
                    "RealTimeProtectionStatus": 0,
                    "CloudQueryStateDescription": "云查离线,TAV在线,系统修复在线",
                    "OsType": 0,
                    "OnlineStatus": 0,
                    "Os": "",
                    "IOAUserName": "",
                    "CloudQueryState": 0,
                    "RiskScanTime": "",
                    "Guid": "10db7225391fa19bade67e4bb3525c9f",
                    "Id": 40,
                    "Ip": "59.37.125.120",
                    "Hacker": 0,
                    "StrVersion": "0.0.0.0",
                    "Utime": "2022-11-18T10:41:02.436675+08:00",
                    "Camera": 0,
                    "Itime": "2022-11-18T10:41:02.421265+08:00",
                    "Sort": 0,
                    "ConnActiveTime": "2022-11-18T11:11:43.723968+08:00"
                },
                {
                    "LocalIpList": "192.168.226.145",
                    "Name": "junming-PC",
                    "GroupFromAuto": 0,
                    "Status": 4,
                    "Desktop": 0,
                    "UDisk": 0,
                    "Download": 0,
                    "SysFile": 0,
                    "Reg": 0,
                    "Proc": 0,
                    "Driver": 0,
                    "Mid": "F1AFD85EC54480393C546B99C7CD014963761895",
                    "OsBits": 64,
                    "OsVersion": "6.1.7601",
                    "MacAddr": "00:0C:29:A8:37:D6",
                    "RiskCount": 0,
                    "VirusVer": "2.0.13645.8300",
                    "SysRepVersion": "2022.09.02.17.55.57",
                    "GroupNamePath": "全网终端.未分组终端",
                    "UserName": "junming",
                    "GroupId": 393,
                    "GroupName": "未分组终端",
                    "RealTimeProtectionStatus": 0,
                    "CloudQueryStateDescription": "云查在线,TAV在线,系统修复在线",
                    "OsType": 0,
                    "OnlineStatus": 1,
                    "Os": "Microsoft Windows 7 旗舰版 ",
                    "IOAUserName": "",
                    "CloudQueryState": 3,
                    "RiskScanTime": "",
                    "Guid": "F1AFD85EC54480393C546B99C7CD0149",
                    "Id": 37,
                    "Ip": "113.108.77.57",
                    "Hacker": 0,
                    "StrVersion": "108.0.13756.61000",
                    "Utime": "2022-11-17T19:21:29.488298+08:00",
                    "Camera": 0,
                    "Itime": "2022-11-17T19:18:45.715127+08:00",
                    "Sort": 0,
                    "ConnActiveTime": "2022-11-17T23:55:32.425538+08:00"
                },
                {
                    "LocalIpList": "",
                    "Name": "",
                    "GroupFromAuto": 0,
                    "Status": 4,
                    "Desktop": 0,
                    "UDisk": 0,
                    "Download": 0,
                    "SysFile": 0,
                    "Reg": 0,
                    "Proc": 0,
                    "Driver": 0,
                    "Mid": "10db7225391fa19bade67e4bb3525c9f63760C1E",
                    "OsBits": 0,
                    "OsVersion": "",
                    "MacAddr": "",
                    "RiskCount": 0,
                    "VirusVer": "",
                    "SysRepVersion": "",
                    "GroupNamePath": "全网终端.未分组终端",
                    "UserName": "",
                    "GroupId": 393,
                    "GroupName": "未分组终端",
                    "RealTimeProtectionStatus": 0,
                    "CloudQueryStateDescription": "云查离线,TAV在线,系统修复在线",
                    "OsType": 0,
                    "OnlineStatus": 0,
                    "Os": "",
                    "IOAUserName": "",
                    "CloudQueryState": 0,
                    "RiskScanTime": "",
                    "Guid": "10db7225391fa19bade67e4bb3525c9f",
                    "Id": 36,
                    "Ip": "59.37.125.120",
                    "Hacker": 0,
                    "StrVersion": "0.0.0.0",
                    "Utime": "2022-11-17T18:25:34.362171+08:00",
                    "Camera": 0,
                    "Itime": "2022-11-17T18:25:34.342111+08:00",
                    "Sort": 0,
                    "ConnActiveTime": "2022-11-17T18:30:21.802511+08:00"
                },
                {
                    "LocalIpList": "192.168.226.144",
                    "Name": "junming-PC",
                    "GroupFromAuto": 0,
                    "Status": 4,
                    "Desktop": 0,
                    "UDisk": 0,
                    "Download": 0,
                    "SysFile": 0,
                    "Reg": 0,
                    "Proc": 0,
                    "Driver": 0,
                    "Mid": "F1AFD85EC54480393C546B99C7CD0149637607BC",
                    "OsBits": 64,
                    "OsVersion": "6.1.7601",
                    "MacAddr": "00:0C:29:A8:37:D6",
                    "RiskCount": 0,
                    "VirusVer": "2.0.13645.8300",
                    "SysRepVersion": "2022.09.02.17.55.57",
                    "GroupNamePath": "全网终端.未分组终端",
                    "UserName": "junming",
                    "GroupId": 393,
                    "GroupName": "未分组终端",
                    "RealTimeProtectionStatus": 0,
                    "CloudQueryStateDescription": "云查在线,TAV在线,系统修复在线",
                    "OsType": 0,
                    "OnlineStatus": 1,
                    "Os": "Microsoft Windows 7 旗舰版 ",
                    "IOAUserName": "",
                    "CloudQueryState": 3,
                    "RiskScanTime": "",
                    "Guid": "F1AFD85EC54480393C546B99C7CD0149",
                    "Id": 34,
                    "Ip": "113.108.77.57",
                    "Hacker": 0,
                    "StrVersion": "108.0.13756.61000",
                    "Utime": "2022-11-17T18:49:20.741762+08:00",
                    "Camera": 0,
                    "Itime": "2022-11-17T18:06:52.916225+08:00",
                    "Sort": 0,
                    "ConnActiveTime": "2022-11-17T19:01:25.882242+08:00"
                }
            ]
        }
    }
}
```

**Example 2: DescribeViruses**

DescribeViruses

Input: 

```
tccli ioa DescribeViruses --cli-unfold-argument  \
    --OsType 0 \
    --OnlineStatus 1 \
    --GroupId 1 \
    --Condition.PageSize 109 \
    --Condition.PageNum 0 \
    --RiskStatus 1
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "AuthFailure.SignatureFailure",
            "Message": "请求签名验证失败，请检查您的签名计算是否正确。"
        },
        "RequestId": "994bd69f-f163-43b6-a32e-29962867c2d1"
    }
}
```

