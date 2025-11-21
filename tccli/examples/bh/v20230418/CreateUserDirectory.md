**Example 1: 创建用户目录**



Input: 

```
tccli bh CreateUserDirectory --cli-unfold-argument  \
    --DirId 523353 \
    --DirName 测试 \
    --Source 0 \
    --SourceName 自建账号 \
    --UserCount 45 \
    --UserOrgSet.0.OrgId 47723 \
    --UserOrgSet.0.OrgName 开发部 \
    --UserOrgSet.0.OrgIdPath 1233.85232.45245 \
    --UserOrgSet.0.OrgNamePath 全网账户.钉钉.开发部 \
    --UserOrgSet.0.UserTotal 12
```

Output: 
```
{
    "Response": {
        "Id": 234,
        "RequestId": "3c123219-cfe9-4722e-b241-22wfrew"
    }
}
```

