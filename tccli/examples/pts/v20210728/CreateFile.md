**Example 1: 创建文件**



Input: 

```
tccli pts CreateFile --cli-unfold-argument  \
    --FileId file-xx \
    --ProjectId project-xx \
    --Kind 0 \
    --Name uin.csv \
    --Size 3896 \
    --Type csv \
    --LineCount 1001 \
    --HeadLines uin 1 2 \
    --TailLines 998 999 1000 \
    --HeaderInFile True \
    --HeaderColumns uin \
    --FileInfos.0.Name  \
    --FileInfos.0.Size 0 \
    --FileInfos.0.Type  \
    --FileInfos.0.UpdatedAt 
```

Output: 
```
{
    "Response": {
        "RequestId": "xx"
    }
}
```

