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
                "CmdList": "xx",
                "Name": "xx",
                "Id": 1
            }
        ],
        "TotalCount": 1,
        "RequestId": "xx"
    }
}
```

