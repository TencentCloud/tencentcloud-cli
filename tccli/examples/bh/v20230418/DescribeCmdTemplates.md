**Example 1: 查询命令模板列表**



Input: 

```
tccli bh DescribeCmdTemplates --cli-unfold-argument  \
    --IdSet 1
```

Output: 
```
{
    "Response": {
        "CmdTemplateSet": [
            {
                "CmdList": "testvalue",
                "Name": "testvalue",
                "Id": 1
            }
        ],
        "TotalCount": 1,
        "RequestId": "c7c79e35-65b9-4c2a-beea-a038fdf8c082"
    }
}
```

