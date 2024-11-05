**Example 1: 查询命令模板列表**



Input: 

```
tccli dasb DescribeCmdTemplates --cli-unfold-argument  \
    --IdSet 1
```

Output: 
```
{
    "Response": {
        "CmdTemplateSet": [
            {
                "Id": 1,
                "Name": "测试模板",
                "CmdList": "rm -rf"
            }
        ],
        "TotalCount": 1,
        "RequestId": "4e7e46fe-c632-4a67-92ac-b9e8228c78ea"
    }
}
```

