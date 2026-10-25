**Example 1: test**



Input: 

```
tccli rum DescribeIssueAffectedUsers --cli-unfold-argument  \
    --AppId sGPZPBrHhKxe \
    --IssueId 9fd1ac8fd9b45044 \
    --Page 1 \
    --PageSize 20 \
    --AppVersion  \
    --Keyword  \
    --OrderKey last_seen \
    --StartTime 1791820800000 \
    --EndTime 1792425599999 \
    --OrderBy desc
```

Output: 
```
{
    "Response": {
        "Result": "{\"Data\":{\"Users\":[],\"Total\":0,\"Page\":1,\"PageSize\":20}}",
        "RequestId": "f1cb7fcf-a0ac-4805-af51-881b5190e9e1"
    }
}
```

