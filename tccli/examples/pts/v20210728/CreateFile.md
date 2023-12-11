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
    --HeadLines abc \
    --TailLines abc \
    --HeaderInFile True \
    --HeaderColumns abc \
    --FileInfos.0.Name abc \
    --FileInfos.0.Size 0 \
    --FileInfos.0.Type abc \
    --FileInfos.0.UpdatedAt 2020-09-22T00:00:00+00:00 \
    --FileInfos.0.FileId abc
```

Output: 
```
{
    "Response": {
        "RequestId": "70805f6a-d7e1-4247-9d5a-fde3afe2b377"
    }
}
```

