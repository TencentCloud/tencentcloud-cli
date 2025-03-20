**Example 1: 查询恶意请求事件列表**

查询恶意请求事件列表

Input: 

```
tccli tcss DescribeRiskDnsList --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "Address": "www.iuyiyo.cc",
                "City": "shenzhen",
                "ClusterID": "cls-dfw3e***",
                "ClusterName": "clsfoo***",
                "ContainerID": "b18a9a372645caefdca4cf9a4e1078122ecf4081bfab0034f85f664b81df0da5",
                "ContainerIsolateOperationSrc": "运行时安全/文件查杀",
                "ContainerName": "/fervent_goodall",
                "ContainerNetStatus": "NORMAL",
                "ContainerNetSubStatus": "NONE",
                "ContainerStatus": "DESTROYED",
                "Description": "发现容器存在访问恶意IP/域名的行为，您的容器可能已经失陷。\n恶意IP/域名可能是黑客的远控服务器、恶意软件下载源、矿池地址等。",
                "EventCount": 1,
                "EventID": 306602,
                "EventStatus": "EVENT_UNDEAL",
                "EventType": "DOMAIN",
                "FoundTime": "2024-09-29 17:27:15",
                "HostID": "acdd5474-6360-4fd4-bfc7-843162cb8116",
                "HostIP": "10.0.1.92",
                "HostName": "k8s-node1",
                "ImageID": "sha256:eeb6ee3f44bd0b5103bb561b4c16bcb82328cfe5809ab675bb17ab3a16c517c9",
                "ImageName": "centos:7",
                "LatestFoundTime": "2024-09-29 17:27:15",
                "NodeID": "mix-GOmf****",
                "NodeName": "k8s-node1",
                "NodeType": "NORMAL",
                "NodeUniqueID": "896e349d-2e7d-4151-a26f-4e9fdafe****",
                "PodIP": "10.0.1.92",
                "PodName": "PodName",
                "PublicIP": "43.138.142.208",
                "Solution": "1.检查容器内的恶意进程及非法端口，删除可疑的启动项和定时任务；\n 2.对容器存在的风险进行排查，如进行漏洞扫描、木马扫描等；\n 3.对容器所使用的的镜像进行加固，并替换运行中的容器。"
            },
            {
                "Address": "www.baidu.com",
                "City": "beijing",
                "ClusterID": "cls-dfw3e***",
                "ClusterName": "clsfoo***",
                "ContainerID": "b18a9a372645caefdca4cf9a4e1078122ecf4081bfab0034f85f664b81df0da5",
                "ContainerIsolateOperationSrc": "运行时安全/文件查杀",
                "ContainerName": "/fervent_goodall",
                "ContainerNetStatus": "NORMAL",
                "ContainerNetSubStatus": "NONE",
                "ContainerStatus": "DESTROYED",
                "Description": "发现容器存在访问恶意IP/域名的行为，您的容器可能已经失陷。\n恶意IP/域名可能是黑客的远控服务器、恶意软件下载源、矿池地址等。",
                "EventCount": 3,
                "EventID": 306601,
                "EventStatus": "EVENT_UNDEAL",
                "EventType": "DOMAIN",
                "FoundTime": "2024-09-29 17:15:41",
                "HostID": "acdd5474-6360-4fd4-bfc7-843162cb8116",
                "HostIP": "10.0.1.92",
                "HostName": "k8s-node1",
                "ImageID": "sha256:eeb6ee3f44bd0b5103bb561b4c16bcb82328cfe5809ab675bb17ab3a16c517c9",
                "ImageName": "centos:7",
                "LatestFoundTime": "2024-09-29 17:19:18",
                "NodeID": "mix-GOmf****",
                "NodeName": "k8s-node1",
                "NodeType": "NORMAL",
                "NodeUniqueID": "896e349d-2e7d-4151-a26f-4e9fdafe****",
                "PodIP": "10.0.1.92",
                "PodName": "PodName",
                "PublicIP": "43.138.142.208",
                "Solution": "1.检查容器内的恶意进程及非法端口，删除可疑的启动项和定时任务；\n 2.对容器存在的风险进行排查，如进行漏洞扫描、木马扫描等；\n 3.对容器所使用的的镜像进行加固，并替换运行中的容器。"
            }
        ],
        "RequestId": "8edec175-6938-41a7-80e1-b685cc37154c",
        "TotalCount": 2
    }
}
```

