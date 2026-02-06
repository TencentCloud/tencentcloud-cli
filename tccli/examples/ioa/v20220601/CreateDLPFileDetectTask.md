**Example 1: 选择指定节点唯一Id**

直接指定节点鉴定文件

Input: 

```
tccli ioa CreateDLPFileDetectTask --cli-unfold-argument  \
    --DownloadUrl https://test.docx \
    --FileName test.docx \
    --FileMd5 68D9AD663AC025E51A59AA488DFFAF91 \
    --BalanceType 2 \
    --SelectNodeIds 7043A9128D2111111111111111
```

Output: 
```
{
    "Response": {
        "Data": {
            "TaskRequestId": [
                "d3d56tbjsehhqaaaaaa"
            ]
        },
        "RequestId": "7f6a43a2-d23c-49bd-884e-ae5e0f5609e9"
    }
}
```

**Example 2: 指定分组唯一Id**

选中分组中一个节点进行鉴定

Input: 

```
tccli ioa CreateDLPFileDetectTask --cli-unfold-argument  \
    --DownloadUrl http://159.75.26.5:27800/store/CommonResource/TemplateFile/38u4ea7u54c1u4ea4u6613u8ba2u5355.docx \
    --FileName 38u4ea7u54c1u4ea4u6613u8ba2u5355.docx \
    --FileMd5 68D9AD663AC025E51A59AA488DFFAF91 \
    --BalanceType 1 \
    --GroupId ioa_default_group_id
```

Output: 
```
{
    "Response": {
        "Data": {
            "TaskRequestId": [
                "d3jha93jsehqamfdn7fg"
            ]
        },
        "RequestId": "5c85b62f-1b85-442e-900a-13896c078ca8"
    }
}
```

