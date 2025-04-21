**Example 1: 保存自定义Logo信息**

上传完Logo图标后，再调用保存生效，接口操作文件过多，耗时比较长，注意文件列表参数，是调用上传Logo接口返回的。

Input: 

```
tccli ioa SaveLogo --cli-unfold-argument  \
    --FileList LogoIconColour LogoIconWhite LogoIconBlack \
    --CNTitle 测试-B iOA \
    --ENTitle Test-B iOA \
    --OsType windows
```

Output: 
```
{
    "Response": {
        "RequestId": "fe2a70c7-3a33-45e8-baed-6aee8d74bb8d"
    }
}
```

