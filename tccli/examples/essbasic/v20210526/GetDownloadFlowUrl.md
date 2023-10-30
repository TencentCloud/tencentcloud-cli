**Example 1: 生成批量下载控制台连接地址**

生成批量下载控制台连接地址

Input: 

```
tccli essbasic GetDownloadFlowUrl --cli-unfold-argument  \
    --Agent.AppId yDwhxUUckp3gl8j5UuFX33LSNozpRsbi \
    --Agent.ProxyOrganizationOpenId org_dianziqian \
    --Agent.ProxyOperator.OpenId n9527 \
    --Agent.ProxyAppId  \
    --DownLoadFlows.0.FileName 2023采购合同 \
    --DownLoadFlows.0.FlowIdList yDwivUUckpor6wtoUuogwQHCAB0ES0pQ yDwi8UUckpo5fz9cUqI6nGwcuTvt9YSh \
    --DownLoadFlows.1.FileName 2023入职合同 \
    --DownLoadFlows.1.FlowIdList yDwivUUckpor6wobUuogwQHvdGfvDi5K yDwFmUUckpst10i3UubBSat8PWOt2iQF yDwFdUUckpswdrniUuzcbXw8N43W6Kcz
```

Output: 
```
{
    "Response": {
        "DownLoadUrl": "https://beta.ess.tencent.cn/contract-mgr?channel=PROXYCHANNEL&expiredTime=1698393037&code=yDwivU**QH1Jir8mgiZ&token=yDwivUUckpo**H1Jir8mgiZ&operate=downloadFlow",
        "RequestId": "d6c869b7-6383-4ae5-8c30-6375f392e7c4"
    }
}
```

