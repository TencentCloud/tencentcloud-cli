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
    --Agent.AppId 7f3497f015042c9a35e0984a9657b0ec \
    --ResourceId yDRvQUUgygqt75qpUuO4zjERW6iCFCEl
```

Output: 
```
{
    "Response": {
        "RequestId": "0218bd4e-541e-45e8-8d1f-76efef6c83d2",
        "TaskId": "20220729152534589282"
    }
}
```

