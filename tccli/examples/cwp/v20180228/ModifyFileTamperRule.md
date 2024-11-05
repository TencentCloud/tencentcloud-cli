**Example 1: 编辑、新增核心文件监控规则**

正常添加规则

Input: 

```
tccli cwp ModifyFileTamperRule --cli-unfold-argument  \
    --Id 1 \
    --Name 禁止特殊文件访问 \
    --Rules.0.ProcessPath /tmp/* \
    --Rules.0.Target /etc/shadow \
    --Rules.0.Action alert \
    --Rules.0.FileAction read \
    --Uuids 1c26308c-5493-4eaf-a817-112ec25f499e \
    --IsGlobal 1 \
    --Status 1 \
    --Level 1 \
    --AddWhiteType cur
```

Output: 
```
{
    "Response": {
        "RequestId": "c741a4fd-776f-499b-85a2-7bc70fd5b92s"
    }
}
```

