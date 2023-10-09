**Example 1: 示例**

正常添加规则

Input: 

```
tccli cwp ModifyFileTamperRule --cli-unfold-argument  \
    --Id 1 \
    --Name abc \
    --Rules.0.ProcessPath abc \
    --Rules.0.Target abc \
    --Rules.0.Action abc \
    --Rules.0.FileAction abc \
    --Uuids abc \
    --IsGlobal 1 \
    --Status 1 \
    --Level 1 \
    --AddWhiteType abc
```

Output: 
```
{
    "Response": {
        "RequestId": "c741a4fd-776f-499b-85a2-7bc70fd5b92s"
    }
}
```

