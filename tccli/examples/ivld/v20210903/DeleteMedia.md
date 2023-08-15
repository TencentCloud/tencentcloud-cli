**Example 1: 成功删除媒资文件**



Input: 

```
tccli ivld DeleteMedia --cli-unfold-argument  \
    --MediaId media-12345678
```

Output: 
```
{
    "Response": {
        "RequestId": "4d608fa8-66a3-4a25-94ce-1b904d4807f3"
    }
}
```

**Example 2: 删除媒资文件失败-媒资文件不存在**



Input: 

```
tccli ivld DeleteMedia --cli-unfold-argument  \
    --MediaId media-a1b2c3d4
```

Output: 
```
{
    "Response": {
        "RequestId": "4d608fa8-66a3-4a25-94ce-1b904d4807f3",
        "Error": {
            "Code": "ResourceNotFound.MediaNotFound",
            "Message": "媒资不存在"
        }
    }
}
```

