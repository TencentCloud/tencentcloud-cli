**Example 1: 查询个人帐号**



Input: 

```
tccli essbasic DescribeFlowFiles --cli-unfold-argument  \
    --Caller.ApplicationId  \
    --Caller.SubOrganizationId  \
    --Caller.OperatorId  \
    --FlowId 
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "FlowId": "",
        "FlowFileInfos": [
            {
                "FileIndex": 1,
                "FileName": "",
                "FileType": "",
                "FileMd5": "",
                "FileSize": 10,
                "CreatedOn": 12345678,
                "Url": ""
            }
        ]
    }
}
```

