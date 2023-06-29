**Example 1: 创建电子文档**

创建流程对应的文档

Input: 

```
tccli ess CreateDocument --cli-unfold-argument  \
    --Operator.UserId 112345678********45678901 \
    --FileNames 文件名 \
    --FlowId c7b5ca37ae*******2b4c6644 \
    --TemplateId 00033ed4d1********a82a9 \
    --ClientToken c5qwe37ae*******g4qw8v1e \
    --NeedPreview True \
    --FormFields.0.ComponentValue 控件填充内容 \
    --FormFields.0.ComponentId 控件ID
```

Output: 
```
{
    "Response": {
        "RequestId": "s123456789",
        "DocumentId": "yDxM6**********KAMwutBsRy",
        "PreviewFileUrl": "https://file.ess.tencent.cn/bresource/resource/resource/0/xxxxxxxxx"
    }
}
```

