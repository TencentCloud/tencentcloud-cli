**Example 1: 查询恶意请求事件详情**



Input: 

```
tccli cwp DescribeRiskDnsEventInfo --cli-unfold-argument  \
    --Id 1
```

Output: 
```
{
    "Response": {
        "Info": {
            "Id": 10368,
            "PolicyId": 0,
            "PolicyType": -1,
            "PolicyName": "policy1",
            "ProtectLevel": 2,
            "HostId": "02db9a21-78fe-4a4c-b96f-a11bf819a962",
            "HostName": "v_llzlu恶意请求",
            "HostIp": "192.168.111.28",
            "WanIp": "43.138.255.181",
            "HostStatus": "OFFLINE",
            "AgentId": "02db9a21-78fe-4a4c-b96f-a11bf819a962",
            "Domain": "183.60.95.201",
            "Tags": [],
            "AccessCount": 1,
            "ThreatDesc": "发现主机存在访问恶意IP/域名的行为，您的主机可能已经失陷。\n恶意IP/域名可能是黑客的远控服务器、恶意软件下载源、矿池地址等。",
            "SuggestSolution": "1.检查恶意进程及非法端口，删除可疑的启动项和定时任务；\n2.隔离或者删除相关的木马文件；\n3.对系统进行风险排查，并进行安全加固，详情可参考如下链接： \n【Linux】https://cloud.tencent.com/document/product/296/9604 \n【Windows】https://cloud.tencent.com/document/product/296/9605",
            "ReferenceLink": "link",
            "HandleStatus": 6,
            "Pid": 1387042,
            "ProcessName": "/usr/bin/ping",
            "ProcessMd5": "7f42e35e3065eaa9a58b89e249e8cbc7",
            "CmdLine": "ping 183.60.95.201 ",
            "FirstTime": "2022-09-19 14:57:23",
            "LastTime": "2022-09-19 14:57:23"
        },
        "RequestId": "083fae4c-ac2c-4e41-ad88-b4420c9fce7c"
    }
}
```

