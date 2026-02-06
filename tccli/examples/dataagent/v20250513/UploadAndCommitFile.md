**Example 1: 上传并提交文件**

上传并提交文件

Input: 

```
tccli dataagent UploadAndCommitFile --cli-unfold-argument  \
    --InstanceId instance001 \
    --CosFiles.0.FileName 1.txt \
    --CosFiles.0.FileType TXT \
    --CosFiles.0.UserCosUrl https://xxxx.cos.ap-chongqing.myqcloud.com/1.txt \
    --KnowledgeBaseId kb001
```

Output: 
```
{
    "Response": {
        "JobId": "job001",
        "RequestId": "162e94d1-97ef-452d-82df-600fa0f3e972"
    }
}
```

