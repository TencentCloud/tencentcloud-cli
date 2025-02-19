**Example 1: 实时文档上传**

实时文档上传

Input: 

```
tccli lkeap UploadDocRealtime --cli-unfold-argument  \
    --KnowledgeBaseId 594669442 \
    --FileName changan-short.doc \
    --FileType DOC \
    --FileUrl https://qidian-qbot-test-1251316161.cos.ap-guangzhou.myqcloud.com/2024-08-20/1251316161/20548499/changan-short.doc?q-sign-algorithm=sha1&q-ak=AKxxxxxxx&q-sign-time=1726245910;1726253110&q-key-time=1726245910;1726253110&q-header-list=&q-url-param-list=&q-signature=114996cce2050ca1edbe6e69606e5c01b4c5a3a1
```

Output: 
```
{
    "IsFinal": true,
    "DocId": "1828430526517084160",
    "Progress": 80,
    "PageNum": 0,
    "Status": "SUCCESS"
}
```

