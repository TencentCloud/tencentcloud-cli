**Example 1: 获取两个合同撤销的腾讯电子签小程序链接**

获取两个合同撤销的腾讯电子签小程序链接

Input: 

```
tccli essbasic ChannelCreateBatchCancelFlowUrl --cli-unfold-argument  \
    --Agent.AppId yDwhxUUckp3gl8j5UuFX33LSNozpRsbi \
    --Agent.ProxyOrganizationOpenId org_diziqain \
    --Agent.ProxyOperator.OpenId n9527 \
    --Agent.ProxyAppId  \
    --FlowIds yDSLKUUckpoqyl0rUyC8ScPwfefxADo9 yDSLKUUckpoq79wpUw8Md4qaPVed40LQ
```

Output: 
```
{
    "Response": {
        "BatchCancelFlowUrl": "https://res.ess.tencent.cn/cdn/h5-activity-beta/jump-mp.html?to=BATCH_REVOKE_FLOW&tokenId=yDSLKUUc*a7KQNiW2&userId=yDwJ5UUckpk*DyBpuGTgVEGzo&expireOn=1699013729&login=1&verify=1",
        "FailMessages": [
            "",
            ""
        ],
        "UrlExpireOn": "2023-11-03 20:15:29",
        "TaskId": "yDCVWUUckpwk3b05UyEZnO0xOn3snWWY",
        "RequestId": "549a7dce-5d89-4797-85c1-d8b2794fcc73"
    }
}
```

