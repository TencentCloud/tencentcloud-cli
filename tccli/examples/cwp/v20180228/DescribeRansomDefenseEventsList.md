**Example 1: 查询防勒索事件列表**

根据过滤参数查询防勒索事件列表

Input: 

```
tccli cwp DescribeRansomDefenseEventsList --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "List": [
            {
                "Id": 74,
                "CreateTime": "2024-05-14 11:01:02",
                "ModifyTime": "2024-07-19 17:59:03",
                "Quuid": "1c26308c-5493-4eaf-a817-112ec25f499e",
                "Uuid": "1c26308c-5493-4eaf-a817-112ec25f499e",
                "Status": 2,
                "BaitFilePath": "/home/.yjfile/121hcXh.doc",
                "FilePath": "/usr/bin/bash",
                "FileMd5": "708c8760385810080c4d17fa84d325ca",
                "FileSize": 964536,
                "Pid": 32254,
                "PidParam": "bash -c echo \"Csip data test\" >> /home/.yjfile/121hcXh.doc  1>&2",
                "Type": 0,
                "PsTree": "W3sicGlkIjozMjI1NCwiZXhlIjoiL3Vzci9iaW4vYmFzaCIsImNtZGxpbmUiOiJiYXNoIC1jIGVjaG8gXCJDc2lwIGRhdGEgdGVzdFwiIFx1MDAzZVx1MDAzZSAvaG9tZS8ueWpmaWxlLzEyMWhjWGguZG9jICAxXHUwMDNlXHUwMDI2MiIsImFjY291bnQiOiIwOjAiLCJzdGFydF90aW1lIjoxNzE1NjU1NjYyLCJleGVfcGVybSI6Ii1yd3hyLXhyLXgiLCJleGVfbXRpbWUiOjE1ODU3MDc0NTEsInNlc3Npb25pZCI6MzIyNTQsInNzaF9zb3VyY2UiOiIxMTMuMTA4Ljc3LjUzOjM5NjIyIiwic3NoX3NlcnZpY2UiOiIxNzIuMTYuNDkuMTA0OjIyIn0seyJwaWQiOjMyMjUyLCJleGUiOiIvdXNyL3NiaW4vc3NoZCIsImNtZGxpbmUiOiIvdXNyL3NiaW4vc3NoZCAtRCAtUiIsImFjY291bnQiOiIwOjAiLCJzdGFydF90aW1lIjoxNzE1NjU1NjYxLCJleGVfcGVybSI6Ii1yd3hyLXhyLXgiLCJleGVfbXRpbWUiOjE2OTExNjQ4NTIsInNlc3Npb25pZCI6MzIyNTJ9XQ==",
                "ProcessStartTime": "2024-05-14 11:01:02",
                "InstanceId": "ins-qwea",
                "HostName": "销售许可测试机器",
                "StrategyId": 5569,
                "StrategyName": "测试勿动",
                "HostIp": "xx.xx.xx.xx",
                "WanIp": "xx.xx.xx.xx",
                "SnapshotNum": 45
            }
        ],
        "RequestId": "4e1f7136-1777-59a3-f31e-ed0623b3d270"
    }
}
```

