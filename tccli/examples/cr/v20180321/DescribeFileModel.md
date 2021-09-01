**Example 1: 查询机器人文件模板**



Input: 

```
tccli cr DescribeFileModel --cli-unfold-argument  \
    --Module AiApi \
    --Operation DescribeFileModel \
    --FileType input \
    --BotName 测试
```

Output: 
```
{
    "Response": {
        "CosUrl": "http://qcos.com/cnc/3004/11/20/123456-csn3333-000-7e8",
        "RequestId": "12345-6789-test-from-rest4api"
    }
}
```

