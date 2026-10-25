**Example 1: 示例**



Input: 

```
tccli rum DescribeIssues --cli-unfold-argument  \
    --AppId 146692 \
    --StartTime 1781420460000 \
    --EndTime 1781679660000 \
    --Env prod \
    --IssueTypes js_error \
    --Statuses Unresolved \
    --Keyword mall \
    --SortBy last_seen \
    --SortOrder desc \
    --Page 1 \
    --PageSize 20
```

Output: 
```
{
    "Response": {
        "Result": "{\"Items\":[],\"Total\":0}",
        "RequestId": "d102e023-2bcf-44f6-a237-2705afcfdb46"
    }
}
```

