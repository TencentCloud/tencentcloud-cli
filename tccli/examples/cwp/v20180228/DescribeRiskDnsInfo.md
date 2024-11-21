**Example 1: 示例**

查询恶意请求详情

Input: 

```
tccli cwp DescribeRiskDnsInfo --cli-unfold-argument  \
    --Id 1
```

Output: 
```
{
    "Response": {
        "RequestId": "5d14133e-4727-4937-b076-6ff1b9a59f14",
        "RiskDnsInfo": {
            "Url": "www.test.com",
            "AccessCount": 7,
            "ProcessName": "/bin/a***",
            "ProcessMd5": "472c65af3f43136472d1a383f5******",
            "GlobalRuleId": 0,
            "UserRuleId": 0,
            "Status": 0,
            "CreateTime": "2024-10-24 09:10:13",
            "MergeTime": "2024-10-24 09:10:27",
            "Quuid": "05f0bcab-726c-4ea4-8109-bcd03d5598f7",
            "Uuid": "05f0bcab-726c-4ea4-8109-bcd03d5598f7",
            "HostIp": "1.1.1.1",
            "Alias": "别名",
            "Description": "未知的APT组织",
            "Id": 10001,
            "Pid": 0,
            "CmdLine": "cmd",
            "Reference": "ref",
            "SuggestScheme": "1、检查恶意进程及非法端口，删除可疑的启动项和定时任务；\n2、隔离或者删除相关的木马文件；\n3、对系统进行风险排查，并进行安全加固，详情可参考如下链接： \n【Linux】https://cloud.tencent.com/document/product/296/9604 \n【Windows】https://cloud.tencent.com/document/product/296/9605",
            "Tags": [
                "apt",
                "apt"
            ],
            "MachineWanIp": "1.1.1.1",
            "MachineStatus": "ONLINE"
        }
    }
}
```

