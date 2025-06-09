**Example 1: 查询终端硬件信息列表**

查询终端硬件信息列表

Input: 

```
tccli ioa DescribeDeviceHardwareInfoList --cli-unfold-argument  \
    --GroupId 11668614 \
    --OsType 0 \
    --DomainInstanceId 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "AccountName": "",
                    "Cpu": "12th Gen Intel(R) Core(TM) i7-12700H",
                    "GroupId": 11668615,
                    "GroupName": "未分组终端",
                    "GroupNamePath": "全网终端.未分组终端",
                    "HardDiskSize": "VMware Virtual NVMe Disk 44 GB",
                    "Id": 288665,
                    "Ip": "113.108.77.52",
                    "MacAddr": "00:0C:29:96:E6:DE",
                    "Memory": "4 GB",
                    "Mid": "0A811A6ECD8D6F4CA516AB56B1C2ECFC68104148",
                    "Monitor": "",
                    "Name": "PC-20240705KXXE",
                    "OsType": 0,
                    "Status": 5,
                    "UserName": "Administrator"
                },
                {
                    "AccountName": "",
                    "Cpu": "Intel Pentium III Xeon 处理器",
                    "GroupId": 11668634,
                    "GroupName": "dddd",
                    "GroupNamePath": "全网终端.dddd",
                    "HardDiskSize": "VMware, VMware Virtual S SCSI Disk Device 14 GB",
                    "Id": 288664,
                    "Ip": "113.108.77.52",
                    "MacAddr": "B0:DC:EF:E7:37:EE",
                    "Memory": "1024 MB",
                    "Mid": "489C698CAECC13B1B7C44E59443F5CBB676B7F33",
                    "Monitor": "",
                    "Name": "cs-207addad83ae",
                    "OsType": 0,
                    "Status": 5,
                    "UserName": "Administrator"
                },
                {
                    "AccountName": "",
                    "Cpu": "12th Gen Intel(R) Core(TM) i7-12700H",
                    "GroupId": 11668637,
                    "GroupName": "本地ip",
                    "GroupNamePath": "全网终端.本地ip",
                    "HardDiskSize": "SAMSUNG MZVL41T0HBLB-00BL7 953 GB",
                    "Id": 288663,
                    "Ip": "119.147.10.192",
                    "MacAddr": "B0:DC:EF:E7:37:EA",
                    "Memory": "32 GB",
                    "Mid": "8314BF3FD3FD738410C4FBB0DDDA48786800AB00",
                    "Monitor": "",
                    "Name": "STEVENSSHE-NBIR",
                    "OsType": 0,
                    "Status": 5,
                    "UserName": "Administrator"
                },
                {
                    "AccountName": "",
                    "Cpu": "",
                    "GroupId": 11668634,
                    "GroupName": "dddd",
                    "GroupNamePath": "全网终端.dddd",
                    "HardDiskSize": "",
                    "Id": 288662,
                    "Ip": "119.147.10.202",
                    "MacAddr": "",
                    "Memory": "",
                    "Mid": "7EBWA5184BEC838B96B29CE8105EC66167F8D1B2",
                    "Monitor": "",
                    "Name": "lucal_win-PC7",
                    "OsType": 0,
                    "Status": 5,
                    "UserName": "lucal_win"
                },
                {
                    "AccountName": "",
                    "Cpu": "",
                    "GroupId": 11668634,
                    "GroupName": "dddd",
                    "GroupNamePath": "全网终端.dddd",
                    "HardDiskSize": "",
                    "Id": 288661,
                    "Ip": "119.147.10.202",
                    "MacAddr": "",
                    "Memory": "",
                    "Mid": "1EBWA5184BEC838B96B29CE8105EC66167F8CFBD",
                    "Monitor": "",
                    "Name": "lucal_win-PC",
                    "OsType": 0,
                    "Status": 5,
                    "UserName": "lucal_win"
                }
            ],
            "Page": {
                "PageCount": 1,
                "PageNum": 1,
                "PageSize": 20,
                "Total": 5
            }
        },
        "RequestId": "e00b7ba5-f534-4067-9fda-83012521919d"
    }
}
```

