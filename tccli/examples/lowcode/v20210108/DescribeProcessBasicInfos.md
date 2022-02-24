**Example 1: 批量查询流程基础信息列表**



Input: 

```
tccli lowcode DescribeProcessBasicInfos --cli-unfold-argument  \
    --Status 0 \
    --ProcessName xx \
    --Limit 0 \
    --ProcessKey xx \
    --EnvId env-001 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Data": {
            "ResponseList": [
                {
                    "Status": 0,
                    "Version": 0,
                    "InvokedCount": 0,
                    "ModifyTime": "xx",
                    "Uin": "xx",
                    "ProcessName": "xx",
                    "ProcessDesc": "xx",
                    "ProcessKey": "xx",
                    "AppId": 0,
                    "SubUin": "xx",
                    "CreateTime": "xx"
                }
            ],
            "TotalCount": 0
        },
        "RequestId": "xx"
    }
}
```

