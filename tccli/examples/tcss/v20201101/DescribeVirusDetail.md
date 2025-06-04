**Example 1: 运行时查询木马文件信息**

运行时查询木马文件信息

Input: 

```
tccli tcss DescribeVirusDetail --cli-unfold-argument  \
    --Id 10021
```

Output: 
```
{
    "Response": {
        "AncestorProcessParam": "/usr/local/bin/containerd-shim-runc-v2 -namespace k8s.io -id 7b4ed805844e07bd15663e4f778acf9bf388719cbcdf794290b9637a550a21d6 -address /run/containerd/containerd.****",
        "AncestorProcessPath": "/usr/local/bin/containerd-shim-run****",
        "AncestorProcessStartUser": "0",
        "AncestorProcessUserGroup": "0",
        "CheckPlatform": [
            "VDC",
            "TAV"
        ],
        "ClientIP": "10.*.*.1",
        "ClusterID": "cls-dfw3e***",
        "ClusterName": "clsfoo***",
        "ContainerId": "d4c43f9268ecea2aa75b26632299df8aaf496a*******",
        "ContainerIsolateOperationSrc": "运行时安全/文件查杀",
        "ContainerName": "/container_name",
        "ContainerNetStatus": "ISOLATED",
        "ContainerNetSubStatus": "NONE",
        "CreateTime": "2024-08-27T03:30:37Z",
        "EventType": "恶意文件告警",
        "FileAccessTime": "2018-02-28T07:45:34Z",
        "FileMd5": "81a7701a194c3a******",
        "FileModifyTime": "2018-02-28T07:45:34Z",
        "FileName": "specimen_*******",
        "FilePath": "/home/virus/specimen_******",
        "HarmDescribe": "蠕虫病毒Ramnit最早出现在2010年，至今已有8年之久，因传播力强而“闻名于世”。",
        "HostIP": "10.0.0.1",
        "HostId": "dc56fda9-58c8-4c4f-9e8c-abb0cd4f92aa",
        "HostName": "hostname",
        "ImageId": "sha256:80beff5ff34259ceb7fbe9cd*******",
        "ImageName": "centos:7",
        "Mark": "mark reason",
        "ModifyTime": "2024-10-21T06:42:49Z",
        "Namespace": "tcss",
        "NodeID": "mix-GOmf****",
        "NodeSubNetCIDR": "10.*.*.1/24",
        "NodeSubNetID": "subnet-aau2***",
        "NodeSubNetName": "subnet***",
        "NodeType": "NORMAL",
        "NodeUniqueID": "wer41324-18a1-4775-9e3f-**",
        "OperationTime": "2024-08-27T03:30:37Z",
        "PProcessParam": "node dist/inde****",
        "PProcessPath": "/usr/bin/****",
        "PProcessStartUser": "root",
        "PProcessUserGroup": "root",
        "PodIP": "10.0.*.*",
        "PodName": "PodName",
        "PodStatus": "Running",
        "ProcessAccountGroup": "root",
        "ProcessArgv": "git clone --depth=1 https://github.com/busi",
        "ProcessChan": "git(433802)|node(280016)|containerd-shim-runc-v2(176637)|system****",
        "ProcessFileAuthority": "-rwxr-****",
        "ProcessId": 0,
        "ProcessMd5": "472c65af3f43136472d1a383f5******",
        "ProcessName": "/bin/a***",
        "ProcessPath": "/usr/bin****",
        "ProcessStartAccount": "root",
        "RequestId": "dc56fda9-58c8-4c4f-9e8c-b7296836*****",
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
        "WorkloadType": "DaemonSet",
        "ContainerStatus": "RUNNING"
    }
}
```

