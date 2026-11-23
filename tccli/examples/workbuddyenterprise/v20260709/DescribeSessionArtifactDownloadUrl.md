**Example 1: 获取目标产物ID的下载地址**

已知对应产物 ID， 需要下载到本地时使用。

Input: 

```
tccli workbuddyenterprise DescribeSessionArtifactDownloadUrl --cli-unfold-argument  \
    --ArtifactId 01a17de6-3743-7e3b-96fa-e4c7505b8b37
```

Output: 
```
{
    "Response": {
        "DownloadUrl": "https://managed-agent-store-1328944842.cos.accelerate.myqcloud.com/managed-agent/artifacts/2026-10/a9b52be44a69d675/3793806491318e7e/01a17de6-3743-7e3b-96fa-e4c7505b8b***********************************************************************************************************************************************************************%3B1793117663&q-key-time=1793114063%3B1793117663&q-header-list=host&q-url-param-list=response-content-disposition&q-signature=18f9219f47591acef678491bd344079883e5bf2d",
        "ExpiredTime": "2026-10-27T16:14:23Z",
        "FileName": "hello_world.py",
        "FileSha256": "*2373fc9647ea86*d12792594f30b*7e**7cc*fd*014cc5ac748ba41b4*****8",
        "FileSizeBytes": 180,
        "RequestId": "5a1eb38a-7991-49c1-9732-4f9e7577da3b"
    }
}
```

