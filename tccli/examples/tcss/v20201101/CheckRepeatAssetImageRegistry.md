**Example 1: 检查单个镜像仓库名是否重复**



Input: 

```
tccli tcss CheckRepeatAssetImageRegistry --cli-unfold-argument  \
    --Name xxx
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "IsRepeat": true
    }
}
```

