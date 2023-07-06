**Example 1: 领取合同**

领取未归属的合同

Input: 

```
tccli essbasic ChannelCreateBoundFlows --cli-unfold-argument  \
    --FlowIds test \
    --Agent.ProxyOperator.OpenId test \
    --Agent.ProxyOrganizationOpenId test \
    --Agent.AppId test
```

Output: 
```
{
    "Response": {
        "RequestId": "s16221xxxx12775546"
    }
}
```

