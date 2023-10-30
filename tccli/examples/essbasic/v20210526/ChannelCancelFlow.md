**Example 1: 撤销签署流程**

撤销签署流程

Input: 

```
tccli essbasic ChannelCancelFlow --cli-unfold-argument  \
    --FlowId yDwiBUUckpo2wjjbUuRr5O4wOuKZNrbr \
    --Agent.AppId yDwhxUUckp3gl8j5UuFX33LSNozpRsbi \
    --Agent.ProxyOrganizationOpenId org_dianziqian \
    --Agent.ProxyOperator.OpenId n9527 \
    --Agent.ProxyAppId  \
    --CancelMessage 因为合同里边的金额填写错误 \
    --CancelMessageFormat 0
```

Output: 
```
{
    "Response": {
        "RequestId": "22c26f54-d604-4b71-9e66-734d02b44237"
    }
}
```

