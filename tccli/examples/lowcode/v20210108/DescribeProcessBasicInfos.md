**Example 1: 批量查询流程基础信息列表**



Input: 

```
tccli lowcode DescribeProcessBasicInfos --cli-unfold-argument  \
    --ProcessKey abc \
    --ProcessName abc \
    --Status 0 \
    --Limit 0 \
    --Offset 0 \
    --EnvType abc \
    --EnvId abc
```

Output: 
```
{
    "Response": {
        "Data": {
            "ResponseList": [
                {
                    "Uin": "abc",
                    "SubUin": "abc",
                    "AppId": 0,
                    "ProcessKey": "abc",
                    "ProcessName": "abc",
                    "ProcessDesc": "abc",
                    "Version": 0,
                    "Status": 0,
                    "ModifyTime": "abc",
                    "CreateTime": "abc",
                    "InvokedCount": 0,
                    "PublishTime": "abc",
                    "NickName": "abc",
                    "Init": true
                }
            ],
            "TotalCount": 0
        },
        "RequestId": "abc"
    }
}
```

