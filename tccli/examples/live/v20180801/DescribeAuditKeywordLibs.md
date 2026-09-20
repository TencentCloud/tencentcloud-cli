**Example 1: 直播审核词库列表**



Input: 

```
tccli live DescribeAuditKeywordLibs --cli-unfold-argument  \
    --Offset 0 \
    --Limit 100 \
    --Name autotest_lib_001
```

Output: 
```
{
    "Response": {
        "Infos": [
            {
                "CreateTime": "2026-09-18T08:00:14Z",
                "Description": "autotest",
                "LibId": "a4cf3b9b-0c17-4155-ac34-d7d26ae20e68",
                "MatchType": "ExactMatch",
                "Name": "autotest_lib_001",
                "Suggestion": "Review"
            }
        ],
        "Total": 1,
        "RequestId": "839aca8d-2c66-4c16-a214-f364b57ada71"
    }
}
```

