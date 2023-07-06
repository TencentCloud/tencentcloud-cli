**Example 1: 多文件上传接口**

多文件上传

Input: 

```
tccli essbasic UploadFiles --cli-unfold-argument  \
    --Agent.AppId abc \
    --Agent.ProxyOrganizationOpenId abc \
    --BusinessType TEMPLATE \
    --FileInfos.0.FileBody iVBORw0KGgoAAAANSUhxxxxAElEQVR4Xu3dbah1W5eQ7HmoAAAAASUVORK5CYII= \
    --FileInfos.0.FileName a.pdf
```

Output: 
```
{
    "Response": {
        "FileIds": [
            "d54e****************A2b7562"
        ],
        "FileUrls": [
            "https://a.b.com/d5****************2b7562"
        ],
        "TotalCount": 1,
        "RequestId": "4fecd****************bdbb7e5"
    }
}
```

