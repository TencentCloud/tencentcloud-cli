**Example 1: 示例**



Input: 

```
tccli es DescribeServerlessSpaceUser --cli-unfold-argument  \
    --SpaceId space-feafaef \
    --Offset 1 \
    --Limit 10 \
    --UserNames admin \
    --UserTypes 0 \
    --PrivilegeTypes 0
```

Output: 
```
{
    "Response": {
        "ServerlessSpaceUsers": [
            {
                "Username": "admin",
                "Password": "fwaifjiajf",
                "CreateTime": "2023-06-22 00:52:58",
                "Status": 1,
                "IndicesScope": [
                    "indexName"
                ],
                "PrivilegeType": 0
            }
        ],
        "TotalCount": 1,
        "RequestId": "40f4f780-9969-42f9-8bd9-ccf0d1f2591a"
    }
}
```

