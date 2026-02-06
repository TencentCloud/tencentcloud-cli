**Example 1: 修改用户目录**



Input: 

```
tccli bh ModifyUserDirectory --cli-unfold-argument  \
    --Id 3 \
    --UserOrgSet.0.OrgId 4712 \
    --UserOrgSet.0.OrgName 测试部 \
    --UserOrgSet.0.OrgIdPath 1233.85232.4712 \
    --UserOrgSet.0.OrgNamePath 全网账户.钉钉.测试部 \
    --UserOrgSet.0.UserTotal 11
```

Output: 
```
{
    "Response": {
        "RequestId": "2edsdg-cfe9-47sf2e-b241-22wfrew"
    }
}
```

