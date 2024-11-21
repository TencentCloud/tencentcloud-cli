**Example 1: 运行时查询木马文件信息**

运行时查询木马文件信息

Input: 

```
tccli tcss DescribeVirusDetail --cli-unfold-argument  \
    --Id dskaldjskld
```

Output: 
```
{
    "Response": {
        "AncestorProcessParam": "-",
        "AncestorProcessPath": "-",
        "AncestorProcessStartUser": "-",
        "AncestorProcessUserGroup": "",
        "CheckPlatform": [
            "VDC",
            "TAV"
        ],
        "ClientIP": "106.55.163.111",
        "ClusterID": "",
        "ClusterName": "",
        "ContainerId": "d4c43f9268ecea2aa75b26632299df8aaf496af54e391f94ebcc62d7b2435105",
        "ContainerIsolateOperationSrc": "运行时安全/文件查杀",
        "ContainerName": "/pedantic_agnesi",
        "ContainerNetStatus": "ISOLATED",
        "ContainerNetSubStatus": "NONE",
        "CreateTime": "2024-08-27T03:30:37Z",
        "EventType": "恶意文件告警",
        "FileAccessTime": "2018-02-28T07:45:34Z",
        "FileMd5": "81a7701a194c3a1179cfe4a7ac836626",
        "FileModifyTime": "2018-02-28T07:45:34Z",
        "FileName": "specimen_a1193b5c213b17cfc7fd",
        "FilePath": "/home/virus/specimen_a1193b5c213b17cfc7fd",
        "HarmDescribe": "蠕虫病毒Ramnit最早出现在2010年，至今已有8年之久，因传播力强而“闻名于世”。Ramnit蠕虫病毒通过被感染的EXE、DLL、HTML、HTM文件传播，在正常电脑打开这些染毒文件时会导致新的感染发生。同时，Ramnit蠕虫病毒还会通过浏览器访问网页、写入U盘移动硬盘，创建U盘自启动等方式进行蠕虫式传播。",
        "HostIP": "172.16.0.34",
        "HostId": "dc56fda9-58c8-4c4f-9e8c-b7296836c1fe",
        "HostName": "稳定性监控_ivon",
        "ImageId": "sha256:80beff5ff34259ceb7fbe9cd10b2d94912618f5b5595f234349c5bb0cd4f9211",
        "ImageName": "centos:7",
        "Mark": "just for test",
        "ModifyTime": "2024-10-21T06:42:49Z",
        "Namespace": "",
        "NodeID": "",
        "NodeSubNetCIDR": "",
        "NodeSubNetID": "",
        "NodeSubNetName": "",
        "NodeType": "NORMAL",
        "NodeUniqueID": "wer41324-18a1-4775-9e3f-cdfc89845157",
        "OperationTime": "2024-08-27T03:30:37Z",
        "PProcessParam": "-",
        "PProcessPath": "-",
        "PProcessStartUser": "-",
        "PProcessUserGroup": "",
        "PodIP": "",
        "PodName": "/",
        "PodStatus": "",
        "ProcessAccountGroup": "",
        "ProcessArgv": "-",
        "ProcessChan": "-",
        "ProcessFileAuthority": "-",
        "ProcessId": 0,
        "ProcessMd5": "-",
        "ProcessName": "",
        "ProcessPath": "-",
        "ProcessStartAccount": "-",
        "RequestId": "dc56fda9-58c8-4c4f-9e8c-b7296836c1f1",
        "RiskLevel": "RISK_CRITICAL",
        "Size": 332155,
        "SourceType": 0,
        "Status": "DEAL_NONE",
        "SubStatus": "FILE_NOT_FOUND",
        "SuggestScheme": "1.在病毒尚未完全清理干净之前，暂时关闭系统文件共享功能 ，防止感染范围进一步扩大；\n2.检查恶意进程及非法端口，删除可疑的启动项和定时任务；\n3.隔离或者删除相关的木马文件；\n4.对系统进行风险排查，并进行安全加固，详情可参考如下链接： \n【Linux】https://cloud.tencent.com/document/product/296/9604 \n【Windows】https://cloud.tencent.com/document/product/296/9605",
        "Tags": [
            "ramnit",
            "Worm",
            "窃取用户信息，感染用户本地所有的html、exe、dll等格式的文件。"
        ],
        "VirusName": "Win32.Virus.Ramnit.Qwhl",
        "WorkloadType": ""
    }
}
```

