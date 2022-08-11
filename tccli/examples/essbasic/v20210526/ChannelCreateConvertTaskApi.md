**Example 1: test示例**



Input: 

```
tccli essbasic ChannelCreateConvertTaskApi --cli-unfold-argument  \
    --ResourceType docx \
    --ResourceName hello.docx \
    --Operator.OpenId test1_clara_test1 \
    --Operator.ClientIp 8.8.8.8 \
    --Operator.ProxyIp  \
    --Agent.ProxyOrganizationOpenId test1_clara_open_organization1 \
    --Agent.AppId 7f3497*********84a9657b0ec \
    --ResourceId yDRvQUUg*********zjERW6iCFCEl
```

Output: 
```
{
    "Response": {
        "RequestId": "0218bd4e-541e-45e8-8d1f-76efef6c83d2",
        "TaskId": "20220*********589282"
    }
}
```

