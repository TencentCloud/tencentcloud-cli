**Example 1: 示例**



Input: 

```
tccli cwp DescribeBashEventsInfo --cli-unfold-argument  \
    --Id 12
```

Output: 
```
{
    "Response": {
        "BashEventsInfo": {
            "BashCmd": "base64 -d",
            "CreateTime": "2024-10-24 16:20:57",
            "DetectBy": "1",
            "Exe": "/usr/bin/base64",
            "HarmDescribe": "黑客在入侵服务器后，为了进行下一步的恶意操作，会执行恶意文件下载、连接矿池、添加公钥、查看敏感文件等操作。",
            "HostIp": "10.*.*.1",
            "Id": 10001,
            "MachineName": "机器名称",
            "MachineStatus": "ONLINE",
            "MachineWanIp": "10.*.*.1",
            "ModifyTime": "2024-10-24 16:20:58",
            "Pid": "5747",
            "Platform": 4,
            "PsTree": "[{\"pid\":5747,\"exe\":\"/usr/bin/base64\",\"account\":\"root:root\",\"cmdline\":\"base64 -d\",\"ssh_service\":\"10.*.*.1\",\"ssh_source\":\"10.*.*.1:2578\",\"start_time\":1729758057,\"type\":1},{\"pid\":4461,\"exe\":\"/usr/bin/bash\",\"account\":\"root:root\",\"cmdline\":\"-bash\",\"ssh_service\":\"10.*.*.1:22\",\"ssh_source\":\"10.*.*.1:2578\",\"start_time\":1729757844,\"type\":2}]",
            "Quuid": "fcf85fc9-f45e-***-bca4-fcae074eda32",
            "References": [],
            "RegexBashCmd": "base64 -d",
            "RuleCategory": 1,
            "RuleId": 0,
            "RuleLevel": 1,
            "RuleName": "sh拦截",
            "Status": 5,
            "SuggestScheme": "1、检查恶意进程及非法端口，删除可疑的启动项和定时任务；\n2、隔离或者删除相关的木马文件；\n3、对系统进行风险排查，并进行安全加固，详情可参考如下链接：xa0\n【Linux】https://cloud.tencent.com/document/product/296/9604xa0\n【Windows】https://cloud.tencent.com/document/product/296/9605",
            "Tags": [],
            "User": "0:0",
            "Uuid": "05f0bcab-726c-4ea4-***-bcd03d5598f7"
        },
        "RequestId": "41030e32-67ec-4f07-858c-432ea384ad5a"
    }
}
```

