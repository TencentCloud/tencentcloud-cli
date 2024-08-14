**Example 1: 创建批量操作企业初始化链接**



Input: 

```
tccli ess CreateBatchInitOrganizationUrl --cli-unfold-argument  \
    --Operator.UserId yDxjOXXgydjfxgnzUuO4zjEWA07rD2xl \
    --OperateTypes OPEN_AUTO_SIGN AUTH_JOIN_ORGANIZATION_GROUP CREATE_SEAL \
    --OrganizationIds yDCpSUUckpao78exUIqrf58JQDTLbbTr yDCpSUUckpao696tUIqrf5x1nPoxNy7C
```

Output: 
```
{
    "Response": {
        "MiniAppPath": "pages/guide/index?to=BATCH_INITIALIZATION_ORGANIZATIONS&shortKey=yDAHpURDfyLc5LgBhXb6",
        "OperateLongUrl": "https://res.ess.tencent.cn/cdn/h5-activity-dev/jump-mp.html?to=BATCH_INITIALIZATION_ORGANIZATIONS&shortKey=yDCHpURDfyLc5LgBhXb6",
        "OperateShortUrl": "https://essurl.cn/zahbUBHxW3",
        "QRCodeUrl": "https://dyn.ess.tencent.cn/imgs/qrcode_urls/batch_initialization_organizations/yDCHHUUckpacc9ijUuXGmVcuzZCNH5pF.png",
        "RequestId": "s1723520103899037060"
    }
}
```

