**Example 1: 检查单个镜像仓库名是否重复**



Input: 

```
tccli tcss CheckRepeatAssetImageRegistry --cli-unfold-argument  \
    --Name test-name
```

Output: 
```
{
    "Response": {
        "RequestId": "8a64a4f9-864c-49c6-adcb-21b483de477a",
        "IsRepeat": true
    }
}
```

