**Example 1: 创建文件转换任务**

创建一个docx文件转换成pdf的任务

Input: 

```
tccli essbasic ChannelCreateConvertTaskApi --cli-unfold-argument  \
    --Agent.AppId yDwhxUUckp3gl8j5UuFX33LSNozpRsbi \
    --Agent.ProxyOrganizationOpenId org_dianziqian \
    --Agent.ProxyOperator.OpenId n9527 \
    --Agent.ProxyAppId  \
    --ResourceType docx \
    --ResourceName 张三的入职合同.docx \
    --ResourceId yDRSRUUgygj6rq2wUuO4zjEyBZ2NHiyT
```

Output: 
```
{
    "Response": {
        "RequestId": "0ab69fd3-db36-4a26-998f-6521c538b36a",
        "TaskId": "yDwivUUckpo2v2bhUx8pIP8vBdA0hGSe"
    }
}
```

