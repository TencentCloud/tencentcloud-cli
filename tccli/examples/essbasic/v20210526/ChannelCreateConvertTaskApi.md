**Example 1: 创建转换任务**

创建一个文件转换任务

Input: 

```
tccli essbasic ChannelCreateConvertTaskApi --cli-unfold-argument  \
    --Agent.ProxyOrganizationOpenId yDxAyUyK****cb7u0jQn0Zh7f7 \
    --Agent.ProxyOperator.OpenId 732aaef****541b89c49e0cc \
    --Agent.AppId ed68bc6***********0214e4e \
    --ResourceType docx \
    --ResourceName hello.docx \
    --ResourceId yDRvQUUg*********zjERW6iCFCEl
```

Output: 
```
{
    "Response": {
        "RequestId": "0218bd4xxxxefef6c83d2",
        "TaskId": "20220*********589282"
    }
}
```

