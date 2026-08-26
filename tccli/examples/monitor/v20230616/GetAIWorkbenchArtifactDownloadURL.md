**Example 1: 获取制品的 COS 预签名下载 URL**



Input: 

```
tccli monitor GetAIWorkbenchArtifactDownloadURL --cli-unfold-argument  \
    --SessionId ses-************ \
    --ArtifactId 08****************************05
```

Output: 
```
{
    "Response": {
        "DownloadURL": "https://ob*****************************",
        "ExpiredAt": "2026-06-02**********",
        "RequestId": "7321c63c-0b6a-460f-bb69-0353fdebd69a"
    }
}
```

