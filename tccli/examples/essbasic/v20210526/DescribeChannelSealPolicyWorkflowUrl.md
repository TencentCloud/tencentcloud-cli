**Example 1: 获取用印审批链接**

获取用印审批链接

Input: 

```
tccli essbasic DescribeChannelSealPolicyWorkflowUrl --cli-unfold-argument  \
    --Agent.AppId yDwhxUUckp3gl8j5UuFX33LSNozpRsbi \
    --Agent.ProxyOrganizationOpenId org_dianziqian \
    --Agent.ProxyOperator.OpenId n9527 \
    --Agent.ProxyAppId  \
    --WorkflowInstanceId yDwiBUUckpo27hh3UuLiduR83BEL3kSb
```

Output: 
```
{
    "Response": {
        "WorkflowUrl": "https://res.ess.tencent.cn/cdn/h5-activity-dev/jump-mp.html?to=SEAL_APPROVE&userId=yDwhxUUckp3gl8j5UuFX33LSNozpRsbi&policyId=yDwhxUUckp3gl8j5UuFX33LSNozpRsbi&instanceId=yDwhxUUckp3gl8j5UuFX33LSNozpRsbi&channelType=AAA",
        "RequestId": "s1696921563375938822"
    }
}
```

