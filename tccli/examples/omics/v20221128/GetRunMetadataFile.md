**Example 1: 获取任务详情文件**



Input: 

```
tccli omics GetRunMetadataFile --cli-unfold-argument  \
    --RunUuid fe92382a-9028-4e0f-8d12-fb11d9ad058c \
    --Key nextflow.log \
    --ProjectId prj-wise-blue-platypus-172468
```

Output: 
```
{
    "Response": {
        "CosSignedUrl": "https://bucket-10000.cos.ap-guangzhou.myqcloud.com/omics/fe92382a-9028-4e0f-8d12-fb11d9ad058c/nextflow.log",
        "RequestId": "b6bc5888-9276-4865-a3dc-bcc11d762300"
    }
}
```

