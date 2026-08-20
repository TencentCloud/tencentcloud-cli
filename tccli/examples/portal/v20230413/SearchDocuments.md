**Example 1: 通过关键词搜索文档**



Input: 

```
tccli portal SearchDocuments --cli-unfold-argument  \
    --Query 怎么购买 \
    --Page 1 \
    --PageSize 10 \
    --ProductName 云服务器
```

Output: 
```
{
    "Response": {
        "Documents": [
            {
                "ProductName": "云服务器",
                "Snippet": "在线迁移概述 ufeff ufeff 在线迁移操作指引 ufeff ufeff 兼容性与工具配置说明 ufeff 云服务器购买页升级 腾讯云云服务器购买页已全新***本2 正文内容加粗1 正文内容斜体1 正文内容加粗2 正文内容加粗斜体2 ufeff 正文内容带下划线1 正文内容带下划线2 ufeff",
                "Title": "发布记录",
                "Url": "https://cloud.tencent.com/document/product/213/40573"
            }
        ],
        "Total": 2,
        "RequestId": "25243310-9d33-4c2c-9f72-de7af6eeac04"
    }
}
```

