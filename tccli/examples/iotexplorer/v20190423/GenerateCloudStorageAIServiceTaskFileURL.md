**Example 1: 获取云存 AI 分析任务输出文件的下载地址**



Input: 

```
tccli iotexplorer GenerateCloudStorageAIServiceTaskFileURL --cli-unfold-argument  \
    --TaskId fb066d7a-baac-4706-acda-058f56f82759 \
    --FileName output.mp4 \
    --ExpireTime 1710487898
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03",
        "FileURL": "https://example.com/output.mp4",
        "ExpireTime": 1710487898
    }
}
```

