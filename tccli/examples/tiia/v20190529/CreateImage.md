**Example 1: 调用失败示例**

调用失败示例

Input: 

```
tccli tiia CreateImage --cli-unfold-argument  \
    --GroupId test_group \
    --EntityId test-entity \
    --PicName test_anme \
    --ImageUrl https://liudhu-9527.cos.ap-guangzhou.myqcloud.com/input
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "FailedOperation.DownloadError",
            "Message": "文件下载失败。"
        },
        "RequestId": "258fb494-54db-4814-80e8-b4d2b75c5c83"
    }
}
```

**Example 2: 调用成功示例**

调用成功示例

Input: 

```
tccli tiia CreateImage --cli-unfold-argument  \
    --GroupId test_group \
    --EntityId test-entity \
    --PicName test_anme \
    --ImageUrl https://liudhu-9527.cos.ap-guangzhou.myqcloud.com/input.jpeg
```

Output: 
```
{
    "Response": {
        "Object": null,
        "RequestId": "49120671-d169-4714-a212-cf755e49fad8"
    }
}
```

