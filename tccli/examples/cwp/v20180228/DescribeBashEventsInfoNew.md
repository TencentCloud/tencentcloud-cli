**Example 1: 查询高危命令详情信息**



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
            "Uuid": "05f0bcab-726c-4ea4-8109-bcd03d5598f7",
            "Id": 10001,
            "Quuid": "05f0bcab-726c-4ea4-8109-bcd03d5598f7",
            "HostIp": "1.1.1.1",
            "Platform": 4,
            "BashCmd": "base64 -d",
            "RuleId": 31390,
            "RuleName": "sh拦截",
            "RuleLevel": 1,
            "Status": 5,
            "CreateTime": "2024-10-24 16:20:58",
            "Exe": "/usr/bin/base64",
            "ModifyTime": "2024-10-24 16:20:58",
            "PsTree": "/bin/sshd",
            "User": "0:0",
            "Pid": "5747",
            "RegexBashCmd": "base64 -d",
            "RuleCategory": 1,
            "MachineName": "机器名称",
            "SuggestScheme": "1.检查恶意进程及非法端口，删除可疑的启动项和定时任务；\n2.隔离或者删除相关的木马文件；\n3.对系统进行风险排查，并进行安全加固，详情可参考如下链接：xa0\n【Linux】https://cloud.tencent.com/document/product/296/9604xa0\n【Windows】https://cloud.tencent.com/document/product/296/9605",
            "HarmDescribe": "黑客在入侵服务器后，为了进行下一步的恶意操作，会执行恶意文件下载、连接矿池、添加公钥、查看敏感文件等操作。",
            "Tags": [],
            "References": [],
            "MachineWanIp": "1.1.1.1",
            "MachineStatus": "ONLINE",
            "MachineType": 2,
            "DetectBy": 1
        },
        "RequestId": "be6f6eec-0825-4e67-ab9a-c8568bbf736c"
    }
}
```

