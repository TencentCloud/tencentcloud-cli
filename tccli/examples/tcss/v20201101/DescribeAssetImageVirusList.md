**Example 1: 查询镜像病毒列表**

查询镜像病毒列表

Input: 

```
tccli tcss DescribeAssetImageVirusList --cli-unfold-argument  \
    --ImageID dskaldjskld
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "List": [
            {
                "CheckPlatform": [],
                "Desc": "发现容器上存在恶意木马，您的容器可能已经失陷。\n恶意木马通常会执行挖矿、文件删除、信息窃取和网络攻击等恶意行为。",
                "FileName": "webshell_2.php",
                "FirstScanTime": "2024-09-02 07:36:15",
                "LatestScanTime": "2024-10-23 16:40:54",
                "Md5": "27501aaed5e639693783321219989889",
                "Path": "/root/webshell_2.php",
                "RiskLevel": 4,
                "Size": 51,
                "Solution": "1.检查恶意进程及非法端口，删除可疑的启动项和定时任务；\n2.隔离或者删除相关的木马文件；\n3.对系统进行风险排查，并进行安全加固，详情可参考如下链接： \n【Linux】https://cloud.tencent.com/document/product/296/9604 \n【Windows】https://cloud.tencent.com/document/product/296/9605",
                "Tags": [],
                "VirusName": "Php.Trojan.Php.Ssmw"
            }
        ],
        "RequestId": "8bc803fd-d85d-47b8-9e2b-9644674be677",
        "VirusScanStatus": 1
    }
}
```

