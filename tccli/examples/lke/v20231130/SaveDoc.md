**Example 1: 保存文档**



Input: 

```
tccli lke SaveDoc --cli-unfold-argument  \
    --BotBizId 2092146264497063168 \
    --FileName 极氪9月销量.md \
    --FileType docx \
    --CosUrl /corp/1813132333428768768/2092146264497063168/doc/gWoLGQkYRULVMriEWGmF-2099856816895833024.md \
    --ETag d41d8cd98f00b204e9800998ecf8427e \
    --CosHash 0 \
    --Size 0 \
    --AttrRange 1 \
    --IsRefer True \
    --Opt 2 \
    --FileId 2099856822767500672
```

Output: 
```
{
    "Response": {
        "DocBizId": "2099857636389263552",
        "DuplicateFileCheckType": 0,
        "ErrorLink": "",
        "ErrorLinkText": "",
        "ErrorMsg": "",
        "RequestId": "1b0824a6-cd5a-456f-8b36-16a02e913a93"
    }
}
```

