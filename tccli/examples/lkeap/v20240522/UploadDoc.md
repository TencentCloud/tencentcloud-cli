**Example 1: 上传无属性标签文档**

上传无属性标签文档

Input: 

```
tccli lkeap UploadDoc --cli-unfold-argument  \
    --KnowledgeBaseId 4901991032 \
    --FileName example.pdf \
    --FileType PDF \
    --FileUrl https://qidian-qbot-1251316161.cos.ap-guangzhou.myqcloud.com/public/example/example.pdf
```

Output: 
```
{
    "Response": {
        "DocId": "1830996257459865536",
        "RequestId": "804c3fe0-05b1-48f9-8003-ab118658fec7"
    }
}
```

