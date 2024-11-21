**Example 1: 获取异常进程列表**



Input: 

```
tccli cwp DescribeRiskProcessEvents --cli-unfold-argument  \
    --Limit 30
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "EventId": 24,
                "HostName": "Public-Main-行致-IT-埃安流量管理与服务平台-后台-MNO业务工程-CVM2",
                "Uuid": "364e2cb6-e3a3-****-9abd-b87711b880e3",
                "HostIp": "10.***.***.248",
                "WanIp": "127.5.**.**",
                "ProcessId": 21595,
                "FilePath": "/dev/shm/dev",
                "CmdLine": "./dev -h 10.***.**.1/24 -m ssh -nopoc -t 200 -o ssh.txt ",
                "StartTime": "2023-09-16 18:28:00",
                "DetectTime": "2023-09-16 18:30:55",
                "VirusName": "Linux.Scanner.Fscan",
                "CheckPlatform": [
                    "1"
                ],
                "VirusTags": [
                    "scanner",
                    "hack_tools"
                ],
                "ThreatDesc": "发现主机上存在黑客工具进程，若不是您的主动行为，您的主机可能已经失陷。 黑客工具通常包含扫描器、爆破工具、密码窃取器等恶意软件程序，会被攻击者用来发起攻击。",
                "SuggestSolution": "1.检查恶意进程及非法端口，删除可疑的启动项和定时任务；\n2.隔离或者删除相关的木马文件；\n3.对系统进行风险排查，并进行安全加固，详情可参考如下链接： \n【Linux】https://**.*.com/document/product/296/9604 \n【Windows】https://cloud.tencent.com/document/product/296/9605",
                "ReferenceLink": "https://cloud.tencent.com/document/product/296/9605",
                "HandleStatus": 3,
                "OnlineStatus": 1,
                "MachineExtraInfo": {
                    "WanIP": "10.*.*.*",
                    "PrivateIP": "10.*.*.*",
                    "NetworkType": 0,
                    "NetworkName": "eth1",
                    "InstanceID": "ins-jvi1gdu0",
                    "HostName": "dataHub"
                }
            }
        ],
        "RequestId": "e8fc6e04-5b3d-405d-ab61-da7cc8be2583",
        "TotalCount": 89
    }
}
```

