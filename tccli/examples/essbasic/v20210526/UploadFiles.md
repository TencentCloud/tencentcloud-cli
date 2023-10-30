**Example 1: 文件上传接口**

上传两个文件

Input: 

```
tccli essbasic UploadFiles --cli-unfold-argument  \
    --Agent.AppId yDwhxUUckp3gl8j5UuFX33LSNozpRsbi \
    --Agent.ProxyOrganizationOpenId org_dianziqian \
    --Agent.ProxyOperator.OpenId n9527 \
    --Agent.ProxyAppId  \
    --BusinessType DOCUMENT \
    --FileInfos.0.FileBody JVBERi0xLjcNCiW1tbW1DQoxIDAgeXBlL(文件内容省略) \
    --FileInfos.0.FileName 2023张三入职合同 \
    --FileInfos.1.FileBody 1DQoxIDAgb2JqDQo8PC9UeXBlvUGFnZ(文件内容省略) \
    --FileInfos.1.FileName 2023张三保密协议
```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "FileIds": [
            "yDwivUUckpo2v2bhUx8pIP8vBdA0hGSe",
            "yDwivUUckpo2v2b8Ux8pIP8CvvGGWvIs"
        ],
        "FileUrls": [
            "https://file.test.ess.tencent.cn/bresource/resource/resource/0/0.PDF?hkey=d13d83**c14",
            "https://file.test.ess.tencent.cn/bresource/resource/resource/0/0.PDF?hkey=d13dee**ad"
        ],
        "RequestId": "0ab69fd3-db36-4a26-998f-6521c538b36a"
    }
}
```

