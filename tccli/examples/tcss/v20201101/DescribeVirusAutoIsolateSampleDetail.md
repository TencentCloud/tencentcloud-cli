**Example 1: 查询木马自动隔离样本详情**



Input: 

```
tccli tcss DescribeVirusAutoIsolateSampleDetail --cli-unfold-argument  \
    --MD5 dskaldjskld
```

Output: 
```
{
    "Response": {
        "HarmDescribe": "发现容器上存在恶意木马，您的容器可能已经失陷。\n恶意木马通常会执行挖矿、文件删除、信息窃取和网络攻击等恶意行为。",
        "KillEngine": [],
        "MD5": "5b98800688cae1533ff965ab31baeab1",
        "ReferenceLink": "https://cloud.tencent.com/document/product/296/9605",
        "RequestId": "a8304c25-f23b-4638-b994-7bb0ba4c5156",
        "RiskLevel": "RISK_CRITICAL",
        "Size": 52,
        "SuggestScheme": "1.检查恶意进程及非法端口，删除可疑的启动项和定时任务；\n2.隔离或者删除相关的木马文件；\n3.对系统进行风险排查，并进行安全加固，详情可参考如下链接： \n【Linux】https://cloud.tencent.com/document/product/296/9604 \n【Windows】https://cloud.tencent.com/document/product/296/9605",
        "Tags": [],
        "VirusName": "Bk.YDWebShell.Php.Small.11100534"
    }
}
```

