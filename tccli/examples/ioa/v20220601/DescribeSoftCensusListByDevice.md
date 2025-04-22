**Example 1: 按终端查看软件统计**



Input: 

```
tccli ioa DescribeSoftCensusListByDevice --cli-unfold-argument  \
    --OsType 0 \
    --GroupId 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "GroupId": 11668634,
                    "SoftNum": 0,
                    "IoaUserName": "",
                    "MacAddr": "",
                    "PiracyRisk": 2,
                    "Mid": "1EBWA5184BEC838B96B29CE8105EC66167F8CFBD",
                    "GroupName": "dddd",
                    "Name": "lucal_win-PC",
                    "Ip": "119.147.10.202",
                    "Id": 288661,
                    "GroupNamePath": "全网终端.dddd",
                    "UserName": "lucal_win"
                },
                {
                    "GroupId": 11668615,
                    "SoftNum": 161,
                    "IoaUserName": "",
                    "MacAddr": "B0:DC:EF:E7:37:EA",
                    "PiracyRisk": 2,
                    "Mid": "8314BF3FD3FD738410C4FBB0DDDA48786800AB00",
                    "GroupName": "未分组终端",
                    "Name": "STEVENSSHE-NBIR",
                    "Ip": "119.147.10.192",
                    "Id": 288663,
                    "GroupNamePath": "全网终端.未分组终端",
                    "UserName": "Administrator"
                },
                {
                    "GroupId": 11668615,
                    "SoftNum": 0,
                    "IoaUserName": "",
                    "MacAddr": "B0:DC:EF:E7:37:EE",
                    "PiracyRisk": 2,
                    "Mid": "489C698CAECC13B1B7C44E59443F5CBB676B7F33",
                    "GroupName": "未分组终端",
                    "Name": "cs-207addad83ae",
                    "Ip": "113.108.77.70",
                    "Id": 288664,
                    "GroupNamePath": "全网终端.未分组终端",
                    "UserName": "Administrator"
                }
            ],
            "Page": {
                "PageSize": 10,
                "PageNum": 1,
                "PageCount": 1,
                "Total": 3
            }
        },
        "RequestId": "8104e997-1a80-4697-afeb-cb2154bb0235"
    }
}
```

