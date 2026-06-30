**Example 1: 创建用户目录**



Input: 

```
tccli bh CreateUserDirectory --cli-unfold-argument  \
    --DirId 899412 \
    --DirName test_ioa \
    --UserOrgSet.0.OrgId 900790 \
    --UserOrgSet.0.OrgName test_ioa_01 \
    --UserOrgSet.0.OrgIdPath 819729.899412.900790 \
    --UserOrgSet.0.OrgNamePath 全网账户.test_ioa.test_ioa_01 \
    --UserOrgSet.0.UserTotal 1 \
    --UserOrgSet.0.BindGroupIds 16786204 \
    --Source 0 \
    --SourceName 自建账户 \
    --UserCount 23 \
    --AutoSync True \
    --SyncCron 0 02 * * *
```

Output: 
```
{
    "Response": {
        "Id": 4294967484,
        "RequestId": "066a0dd2-55a9-4602-82e6-145d5faccf1e"
    }
}
```

