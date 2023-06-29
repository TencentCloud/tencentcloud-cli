**Example 1: CreateCloudRunEnv**

创建环境

Input: 

```
tccli tcbr CreateCloudRunEnv --cli-unfold-argument  \
    --Alias xx \
    --FreeQuota xx \
    --Flag xx \
    --VpcId xx \
    --SubNetIds xx \
    --ReqKey xx \
    --PackageType xx \
    --Source xx \
    --Channel xx \
    --EnvId xx
```

Output: 
```
{
    "Response": {
        "EnvId": "prod-3g69bdvme2ac11cb",
        "TranId": "0ow89eea326",
        "RequestId": "1db46cfe-3b3d-47e8-aff2-1cbf1b6c3018"
    }
}
```

**Example 2: success**



Input: 

```
tccli tcbr CreateCloudRunEnv --cli-unfold-argument  \
    --VpcId 字符串 \
    --Alias 字符串 \
    --SubNetIds 字符串 \
    --FreeQuota 字符串 \
    --EnvId 字符串 \
    --Source 字符串 \
    --Flag 字符串 \
    --PackageType 字符串 \
    --ReqKey 字符串 \
    --Channel 字符串
```

Output: 
```
{
    "Response": {
        "EnvId": "env-test",
        "RequestId": "c8b68d5a-d045-4740-b731-da71512be06e",
        "TranId": ""
    }
}
```

