**Example 1: 修改媒体库配置项**



Input: 

```
tccli smh ModifyLibrary --cli-unfold-argument  \
    --Remark 新备注 \
    --LibraryId smh1jjexrwwoa9ok \
    --LibraryExtension.EnableFileHistory true \
    --LibraryExtension.UseRecycleBin true \
    --Name 新名字
```

Output: 
```
{
    "Response": {
        "RequestId": "8dfefe57-2188-4e66-b5ef-07e493b003ce"
    }
}
```

