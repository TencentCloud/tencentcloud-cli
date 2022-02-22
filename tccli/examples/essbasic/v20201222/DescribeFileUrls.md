**Example 1: 预览流程文档**



Input: 

```
tccli essbasic DescribeFileUrls --cli-unfold-argument  \
    --Caller.ApplicationId  \
    --Caller.SubOrganizationId  \
    --Caller.OperatorId  \
    --BusinessIds ac5ff24286c29c9bdca5962003b182d8 ac5ff24286c29c9bdca5962003b182d9 \
    --FileType PDF \
    --BusinessType DOCUMENT \
    --FileName 西安合同 \
    --ResourceLimit 0 \
    --ResourceOffset 0
```

Output: 
```
{
    "Response": {
        "FileUrls": [
            {
                "Url": "https://file.ess.myqcloud.com/files/DOCUMENT/11114444***,12315215515,12415251512/0/0.ZIP?key=1a153dbfb56f46c8653b901a60009589",
                "Index": 1,
                "FlowId": "xxx",
                "Option": "{\"width\":595,\"height\":842}"
            }
        ],
        "TotalCount": 1,
        "RequestId": "s1609900397586332188"
    }
}
```

