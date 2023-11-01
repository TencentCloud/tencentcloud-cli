**Example 1: 获取源站组列表**

获取指定源站组ID的源站组列表

Input: 

```
tccli teo DescribeOriginGroup --cli-unfold-argument  \
    --Filters.0.Name origin-group-id \
    --Filters.0.Values origin-057c4d82-383c-11ee-8888-525400682e90
```

Output: 
```
{
    "Response": {
        "OriginGroups": [
            {
                "CreateTime": "2023-08-11T19:41:33Z",
                "GroupId": "origin-057c4d82-383c-11ee-8888-525400682e90",
                "HostHeader": "",
                "Name": "test_ruichaolin",
                "Records": [
                    {
                        "Private": false,
                        "PrivateParameters": [],
                        "Record": "4.4.4.4",
                        "RecordId": "record-3492ee3b-383c-11ee-8888-525400682e90",
                        "Type": "IP_DOMAIN",
                        "Weight": 40
                    }
                ],
                "References": [],
                "Type": "HTTP",
                "UpdateTime": "2023-08-11T19:41:33Z"
            }
        ],
        "RequestId": "a2e38df8-5800-4495-bd61-b6761b070d50",
        "TotalCount": 1
    }
}
```

