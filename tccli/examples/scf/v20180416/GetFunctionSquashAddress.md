**Example 1: 获取用于下载可执行文件地址**



Input: 

```
tccli scf GetFunctionSquashAddress --cli-unfold-argument  \
    --VersionID xx \
    --FunctionID xx \
    --Qualifier xx
```

Output: 
```
{
    "Response": {
        "CodeUrl": "abc",
        "LayerUrl": "abc",
        "RequestId": "abc"
    }
}
```

