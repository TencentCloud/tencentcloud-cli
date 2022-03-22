**Example 1: 多文件上传接口**



Input: 

```
tccli essbasic UploadFiles --cli-unfold-argument  \
    --Agent.ProxyAppId xx \
    --Agent.ProxyOperator.OpenId xx \
    --Agent.ProxyOperator.ClientIp xx \
    --Agent.ProxyOperator.CustomUserId xx \
    --Agent.ProxyOperator.ProxyIp xx \
    --Agent.ProxyOperator.Channel xx \
    --Agent.ProxyOrganizationId xx \
    --Agent.AppId xx \
    --BusinessType TEMPLATE \
    --FileInfos.0.FileBody iVBORw0KGgoAAAANSUhEUgAAATsAAALGCAYAAAA6ODadAAAgAElEQVR4Xu3dbah1W5eQ7HmoAAAAASUVORK5CYII= \
    --FileInfos.0.FileName a.pdf
```

Output: 
```
{
    "Response": {
        "FileIds": [
            "d54e3caec25ad0ea6be24406762b7562"
        ],
        "FileUrls": [
            "https://a.b.com/d54e3caec25ad0ea6be24406762b7562"
        ],
        "TotalCount": 1,
        "RequestId": "4fecde8c3137d320e8a3c8136bdbb7e5"
    }
}
```

