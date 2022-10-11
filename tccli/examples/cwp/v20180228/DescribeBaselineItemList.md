**Example 1: 检测项结果**



Input: 

```
tccli cwp DescribeBaselineItemList --cli-unfold-argument  \
    --Limit 1 \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "ItemId": 3077,
                "ItemName": "确保未启用DNS服务",
                "CategoryId": 19,
                "ItemDesc": "域名系统（DNS）是一种分层命名系统，它将名称映射到IP地址，以连接到网络的计算机，服务和其他资源。\n",
                "FixMethod": "运行以下命令以禁用named：\n# systemctl disable bind9",
                "RuleName": "国际标准-Ubuntu 16安全基线检查Level1",
                "DetectResultDesc": "",
                "Level": 2,
                "CanBeFixed": 0,
                "DetectStatus": 3,
                "HostName": "功能测试ubuntu16漏洞修复v_txmitan",
                "HostIp": "172.23.16.14",
                "HostId": "044889f8-d6a2-4fc3-a8a8-c114b6f5266b",
                "WanIp": "10.104.9.1",
                "LastTime": "2022-08-22 09:48:42",
                "FirstTime": "2022-08-06 09:43:07",
                "Uuid": "044889f8-d6a2-4fc3-a8a8-c114b6f5266b"
            }
        ],
        "RequestId": "3a2b20bc-2e93-46b3-8bb7-b655aa249c00",
        "Total": 8412
    }
}
```

