**Example 1: 创建数据流动**



Input: 

```
tccli cfs CreateDataFlow --cli-unfold-argument  \
    --FileSystemId cfs-44d53b63e \
    --SourceStorageType S3_COS \
    --SourceStorageAddress https://aileen-data-flow-1251000004.cos.ap-guangzhou.myqcloud.com \
    --SourcePath test3 \
    --TargetPath /cfs/test11 \
    --SecretId AKIDbzzYj65vue75sC1yg8P4cyBHBpLk \
    --SecretKey onE8m9NN82ik6h3FCvXt2uc3Sjp \
    --DataFlowName test
```

Output: 
```
{
    "Response": {
        "DataFlowId": "cfs-dataflow-4f827203",
        "RequestId": "c5369436-a47c-4504-9cfa-f1f40c2c969f"
    }
}
```

