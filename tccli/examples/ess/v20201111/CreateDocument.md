**Example 1: 创建电子文档**



Input: 

```
tccli ess CreateDocument --cli-unfold-argument  \
    --Operator.Channel string \
    --Operator.ClientIp 1.1.1.1 \
    --Operator.OpenId 321654 \
    --Operator.ProxyIp 2.2.2.2 \
    --Operator.UserId 112345678********45678901 \
    --FileNames 123 456 \
    --FlowId 1234 \
    --TemplateId 00033ed4d1********a82a9 \
    --ClientToken 我是token \
    --NeedPreview True \
    --FormFields.0.ComponentValue 控件填充内容 \
    --FormFields.0.ComponentId 控件ID
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "DocumentId": "yDxM6**********KAMwutBsRy",
        "PreviewFileUrl": "https://file.ess.tencent.cn/bresource/resource/resource/0/xxxxxxxxx"
    }
}
```

