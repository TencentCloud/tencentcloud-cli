**Example 1: 批量查询流程折叠基础信息列表**



Input: 

```
tccli lowcode DescribeFoldProcessBasicInfos --cli-unfold-argument  \
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
        "RequestId": "xx",
        "Data": {
            "TotalCount": 31,
            "ResponseList": [
                {
                    "Uin": "11",
                    "AppId": "11",
                    "SubUin": "11",
                    "NickName": "",
                    "ProcessKey": "p11",
                    "ProcessName": "p name",
                    "ProcessDesc": "desc xx",
                    "Version": 1,
                    "Status": 4,
                    "ModifyTime": "2021-07-29T20:32:21.000+0800",
                    "CreateTime": "2021-07-27T22:19:53.000+0800",
                    "PublishTime": "2021-07-29T20:32:22.000+0800",
                    "SubProcessBasicInfoList": [
                        {
                            "Uin": "11",
                            "AppId": "11",
                            "SubUin": "11",
                            "NickName": "",
                            "ProcessKey": "p11",
                            "ProcessName": "p name",
                            "ProcessDesc": "desc xx",
                            "Version": 2,
                            "Status": 3,
                            "ModifyTime": "2021-07-29T20:32:15.000+0800",
                            "CreateTime": "2021-07-27T22:19:53.000+0800"
                        }
                    ]
                }
            ]
        }
    }
}
```

