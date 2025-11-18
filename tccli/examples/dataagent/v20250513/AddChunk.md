**Example 1: 文档切片新增**

文档切片新增

Input: 

```
tccli dataagent AddChunk --cli-unfold-argument  \
    --InstanceId dataagent-hLhMpd0H \
    --FileId 3fd5442a-2764-4f3d-a589-5399ce087284 \
    --Content this is  my test. \
    --AfterChunkId 64bd3527-6ad9-4eda-a809-4e1a7ecaf86a
```

Output: 
```
{
    "Response": {
        "ChunkId": "9b8f5ab2-70a8-49ee-a33a-08eef6ad2470",
        "RequestId": "0b1fb527-a614-40f3-87dc-b58318fe7d24"
    }
}
```

