**Example 1: success**



Input: 

```
tccli tcbr CreateCloudRunEnv --cli-unfold-argument  \
    --VpcId vpc-sdfsdf \
    --Alias sldfjkdlkj \
    --FreeQuota  \
    --EnvId env-sdfsdf \
    --Source wechat \
    --Flag  \
    --PackageType Trial \
    --ReqKey seqId \
    --Channel wechat
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

