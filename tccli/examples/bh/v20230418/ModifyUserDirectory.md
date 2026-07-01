**Example 1: 修改用户目录**



Input: 

```
tccli bh ModifyUserDirectory --cli-unfold-argument  \
    --Id 4294967478 \
    --UserOrgSet.0.OrgId 900790 \
    --UserOrgSet.0.OrgName test_ioa_01 \
    --UserOrgSet.0.OrgIdPath 819729.899412.900790 \
    --UserOrgSet.0.OrgNamePath 全网账户.test_ioa.test_ioa_01 \
    --UserOrgSet.0.UserTotal 1 \
    --AutoSync True \
    --SyncCron 00 02 * * *
```

Output: 
```
{
    "Response": {
        "RequestId": "b5a8f379-c2a7-46d5-8841-89b09ea07026"
    }
}
```

