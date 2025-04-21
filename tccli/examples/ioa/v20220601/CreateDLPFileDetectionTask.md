**Example 1: 送检任务示例**

提交文件送检，之后可用查询文件检测结果接口DescribeDLPFileDetectResult，或在控制台日志上查询结果

Input: 

```
tccli ioa CreateDLPFileDetectionTask --cli-unfold-argument  \
    --Url https://raw.githubusercontent.com/ZhangYang5158/testDLP/refs/heads/testDLP_new/DLP%E6%B5%8B%E8%AF%95%E6%A0%B7%E6%9C%AC.zip \
    --FileName DLP测试样本.zip \
    --FileMd5 e9e7cad967c0c7e22e44789110205111
```

Output: 
```
{
    "Response": {
        "Data": {
            "DLPFileDetectionTaskID": "053a8fe1-150f-434c-b8e9-f1d7804ded1f"
        },
        "RequestId": "053a8fe1-150f-434c-b8e9-f1d7804ded1f"
    }
}
```

