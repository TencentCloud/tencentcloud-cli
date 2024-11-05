**Example 1: 查询本地提权详情**



Input: 

```
tccli cwp DescribePrivilegeEventInfo --cli-unfold-argument  \
    --Id 12
```

Output: 
```
{
    "Response": {
        "PrivilegeEventInfo": {
            "Uuid": "05f0bcab-726c-4ea4-8109-bcd03d5598f7",
            "UserName": "root",
            "UserGroup": "1000",
            "ProcessName": "privilege",
            "CmdLine": "./privilege",
            "ParentProcName": "bash",
            "ParentProcUser": "1000",
            "CreateTime": "2024-09-06 14:17:45",
            "Status": 0,
            "FullPath": "/tmp/privilege",
            "ParentProcGroup": "1000",
            "ParentProcPath": "/usr/bin/bash",
            "PsTree": "[{\"pid\":32528,\"exe\":\"/tmp/a.out\",\"account\":\"root:1002\",\"cmdline\":\"/tmp/a.out\",\"ssh_service\":\"172.16.49.104:22\",\"ssh_source\":\"113.108.77.53:12753\",\"start_time\":1715655696}]",
            "NewCaps": "SYS_RAWIO|DAC_OVERRIDE|DAC_READ_SEARCH|FOWNER|FSETID|KILL|SETGID|SETUID|SETPCAP|LINUX_IMMUTABLE|NET_BIND_SERVICE|NET_BROADCAST|NET_ADMIN|NET_RAW|IPC_LOCK|IPC_OWNER|SYS_MODULE|CHOWN|BLOCK_SUSPEND|WAKE_ALARM|SYSLOG|MAC_ADMIN|MAC_OVERRIDE|SETFCAP|AUDIT_CONTROL|AUDIT_WRITE|LEASE|MKNOD|SYS_TTY_CONFIG|SYS_TIME|SYS_RESOURCE|SYS_NICE|SYS_BOOT|SYS_ADMIN|SYS_PACCT|SYS_PTRACE|SYS_CHROOT",
            "ModifyTime": "2024-09-06 14:17:45",
            "MachineName": "机器名称",
            "ProcFilePrivilege": "-rwsr-xr-x",
            "HostIp": "1.1.1.1",
            "Quuid": "05f0bcab-726c-4ea4-8109-bcd03d5598f7",
            "Id": 10001,
            "MachineWanIp": "1.1.1.1",
            "SuggestScheme": "1、检查系统是否被添加新用户，或者存在异常权限用户；\n2、检查恶意进程及非法端口，删除可疑的启动项和定时任务；\n3.隔离或者删除相关的木马文件；\n4.对系统进行风险排查，并进行安全加固，详情可参考如下链接：xa0\n【Linux】https://cloud.tencent.com/document/product/296/9604xa0\n【Windows】https://cloud.tencent.com/document/product/296/9605",
            "HarmDescribe": "黑客在入侵服务器后，为了进行下一步的恶意操作，会通过特定漏洞提升用户权限，或者直接获取root用户权限。",
            "Tags": [],
            "References": [],
            "MachineStatus": "ONLINE"
        },
        "RequestId": "f7f4d0bc-171d-491e-b97b-5c9bcb5a52a0"
    }
}
```

