**Example 1: 查询恶意请求事件详情**

查询恶意请求事件详情

Input: 

```
tccli tcss DescribeRiskDnsEventDetail --cli-unfold-argument  \
    --EventID 1
```

Output: 
```
{
    "Response": {
        "Address": "www.iuyiyo.cc",
        "AncestorProcessParam": "/usr/bin/containerd-shim-runc-v2 -namespace moby -id b18a9a372645caefdca4cf9a4e1078122ecf4081bfab0034f85f664b81df0da5 -address /run/containerd/containerd.sock",
        "AncestorProcessPath": "/usr/bin/containerd-shim-runc-v2",
        "AncestorProcessStartUser": "root",
        "AncestorProcessUserGroup": "0:0",
        "City": "103",
        "ClusterID": "cls-dfw3e***",
        "ClusterName": "clsfoo***",
        "ContainerID": "b18a9a372645caefdca4cf9a4e1078122ecf4081bfab0034f85f664b81df0da5",
        "ContainerIsolateOperationSrc": "运行时安全/文件查杀",
        "ContainerName": "/fervent_goodall",
        "ContainerNetStatus": "NORMAL",
        "ContainerNetSubStatus": "NONE",
        "ContainerStatus": "RUNNING",
        "Description": "发现容器存在访问恶意IP/域名的行为，您的容器可能已经失陷。\n恶意IP/域名可能是黑客的远控服务器、恶意软件下载源、矿池地址等。",
        "EventCount": 1,
        "EventID": 306602,
        "EventStatus": "EVENT_UNDEAL",
        "EventType": "DOMAIN",
        "FeatureLabel": "label1",
        "FoundTime": "2024-09-29 17:27:15",
        "HostID": "acdd5474-6360-4fd4-bfc7-843162cb8116",
        "HostIP": "10.0.1.233",
        "HostName": "k8s-node1",
        "ImageID": "sha256:eeb6ee3f44bd0b5103bb561b4c16bcb82328cfe5809ab675bb17ab3a16c517c9",
        "ImageName": "centos:7",
        "LatestFoundTime": "2024-09-29 17:27:15",
        "MatchRuleType": "USER",
        "Namespace": "tcss",
        "NodeID": "mix-GOmf****",
        "NodeName": "k8s-node1",
        "NodeSubNetCIDR": "10.0.200.0/24",
        "NodeSubNetID": "subnet-5gu2***",
        "NodeSubNetName": "subnet***",
        "NodeType": "NORMAL",
        "NodeUniqueID": "896e349d-2e7d-4151-a26f-4e9fdafe****",
        "OperationTime": "2024-09-29 17:27:17",
        "ParentProcessParam": "/bin/bash",
        "ParentProcessPath": "/usr/bin/bash",
        "ParentProcessStartUser": "root",
        "ParentProcessUserGroup": "root:root",
        "PodIP": "10.0.1.92",
        "PodName": "PodName",
        "PodStatus": "Running",
        "ProcessAuthority": "-rwxr-xr-x",
        "ProcessMd5": "b8b1ce2ef81accb7febb8ab7f56c1576",
        "ProcessParam": "curl www.iuyiyo.cc",
        "ProcessPath": "/usr/bin/curl",
        "ProcessStartUser": "root",
        "ProcessTree": "curl(2206566)_bash(2178914)_containerd-shim-runc-v2(2178890)_systemd(1)",
        "ProcessUserGroup": "root:root",
        "PublicIP": "43.138.142.208",
        "Reference": [
            "Reference"
        ],
        "Remark": "myremark***",
        "RequestId": "52fe1ea9-4826-4f8e-bc8b-61faae09683b",
        "Solution": "1.检查容器内的恶意进程及非法端口，删除可疑的启动项和定时任务；\n 2.对容器存在的风险进行排查，如进行漏洞扫描、木马扫描等；\n 3.对容器所使用的的镜像进行加固，并替换运行中的容器。",
        "WorkloadType": "DaemonSet"
    }
}
```

