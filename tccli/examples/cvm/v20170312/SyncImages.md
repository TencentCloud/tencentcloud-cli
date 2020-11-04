**Example 1: 同步镜像**

同步镜像img-o3ycss2p到广州

Input: 

```
tccli cvm SyncImages --cli-unfold-argument  \
    --ImageIds img-o3ycss2p\
    --DestinationRegions ap-guangzhou
```

Output: 
```
{
    "Response": {
        "RequestId": "71e69b56-32be-4412-ab45-49eded6a87be"
    }
}
```

