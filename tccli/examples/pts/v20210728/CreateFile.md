**Example 1: 创建场景与文件的关联关系**



Input: 

```
tccli pts CreateFile --cli-unfold-argument  \
    --FileId file-235c3000 \
    --ProjectId project-btksohr0 \
    --Kind 1 \
    --Name abc.csv \
    --Size 100 \
    --Type csv \
    --LineCount 10 \
    --HeadLines head-line-content \
    --TailLines tail-line-content \
    --HeaderInFile True \
    --HeaderColumns header-columns-content \
    --FileInfos.0.Name file-name \
    --FileInfos.0.Size 0 \
    --FileInfos.0.Type file-type \
    --FileInfos.0.UpdatedAt 2020-09-22T00:00:00+00:00 \
    --FileInfos.0.FileId file-1a2b3c4d
```

Output: 
```
{
    "Response": {
        "RequestId": "abc-123-xyz"
    }
}
```

