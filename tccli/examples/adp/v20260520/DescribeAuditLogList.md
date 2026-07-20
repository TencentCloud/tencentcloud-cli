**Example 1: 查看操作日志列表**



Input: 

```
tccli adp DescribeAuditLogList --cli-unfold-argument  \
    --SpaceId default_space \
    --Limit 100 \
    --SearchAfter 1783921991000 \
    --FilterList.0.Name SpaceId \
    --FilterList.0.ValueList default_space
```

Output: 
```
{
    "Response": {
        "AuditLogList": [
            {
                "AccountInfo": {
                    "AccountUin": "700002740513",
                    "Avatar": "https://qidian-qbot-1251316161.cos.ap-guangzhou.myqcloud.com/public/avatar_rabbit02.png",
                    "NickName": "lzh"
                },
                "Action": "删除",
                "AppId": "2076544889342907904",
                "AppName": "eval-workflow-import-exec-043725",
                "Biz": "应用",
                "Content": "删除-eval-workflow-import-exec-043725",
                "OperateTime": "1783921986",
                "UniqueId": "681107ec7e52b226a405577470e5a270e764eeb223ed6c58d0c76880509e86d5"
            }
        ],
        "SearchAfter": [
            "1783917826000"
        ],
        "RequestId": "13c6ac76-9413-462b-a589-63177cb9e4d4"
    }
}
```

