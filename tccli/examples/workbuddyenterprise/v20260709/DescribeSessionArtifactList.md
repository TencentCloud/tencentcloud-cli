**Example 1: 查询指定Session的产物列表**

查询指定会话（SessionID）产物列表，可从 Offset 开始筛选共计 Limit 个产物，并返回产物列表。

Input: 

```
tccli workbuddyenterprise DescribeSessionArtifactList --cli-unfold-argument  \
    --SessionId 2115095472771747840 \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "ArtifactSet": [],
        "TotalCount": 1,
        "RequestId": "4a4d3e20-a6f2-453d-b723-485a427caa51"
    }
}
```

