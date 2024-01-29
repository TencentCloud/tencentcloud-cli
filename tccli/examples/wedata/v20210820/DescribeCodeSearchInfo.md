**Example 1: demo**

全局搜索

Input: 

```
tccli wedata DescribeCodeSearchInfo --cli-unfold-argument  \
    --SearchScope orchrestrationSpace \
    --PageSize 10 \
    --Keyword hannah \
    --SearchScopes orchrestrationSpace \
    --ProjectId 1 \
    --PageNumber 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "CodeSearchInfoList": {
                "Rows": [
                    {
                        "Id": "abc",
                        "Name": "abc",
                        "Type": "abc",
                        "Content": [
                            {
                                "Number": 1,
                                "Line": "abc",
                                "NodeType": "abc"
                            }
                        ],
                        "OwnerName": "abc",
                        "UpdateTime": "abc",
                        "CreateTime": "abc",
                        "MatchRows": 1
                    }
                ],
                "TotalCount": 1
            },
            "DevCount": 1,
            "ScheduleCount": 1,
            "RecycleCount": 1
        },
        "RequestId": "abc"
    }
}
```

