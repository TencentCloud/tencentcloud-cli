**Example 1: 创建PDF拆分任务**

对外部在线文档进行拆分

Input: 

```
tccli lkeap CreateSplitDocumentFlow --cli-unfold-argument  \
    --FileType PDF \
    --FileName example.pdf \
    --FileUrl https://qidian-qbot-1251316161.cos.ap-guangzhou.myqcloud.com/public/example/example.pdf \
    --FileStartPageNumber 1 \
    --FileEndPageNumber 2 \
    --Config.EnableMllm True
```

Output: 
```
{
    "Response": {
        "RequestId": "5e148c27-9c21-43cd-992c-799117bb4216",
        "TaskId": "236e51fd-827b-41cb-b303-56003a817ce5"
    }
}
```

