**Example 1: 模型安装接口调用样例**



Input: 

```
tccli es InstallInstanceModel --cli-unfold-argument  \
    --InstanceId es-ria27gbk \
    --ModelNames bge-base-zh-v1.5 \
    --TaskTypes text_embedding \
    --ModelDescription test model \
    --ModelSourceType PlatformModel \
    --UploadedCosPaths /UserModels/common/bge-base-zh-v1.5.tar.gz
```

Output: 
```
{
    "Response": {
        "FlowId": "4294967526",
        "RequestId": "efbad3b5-5548-47bb-a88a-173adf833c26"
    }
}
```

