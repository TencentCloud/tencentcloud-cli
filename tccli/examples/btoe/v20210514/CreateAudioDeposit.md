**Example 1: 音频文件存证**

用户通过本接口向BTOE写入待存证的音频原文件或下载URL，BTOE对音频原文件存储后，将其Hash值存证上链。

Input: 

```
tccli btoe CreateAudioDeposit --cli-unfold-argument  \
    --BusinessId as1111323311 \
    --EvidenceName 存证名称 \
    --FileContent  \
    --FileName  \
    --EvidenceHash  \
    --HashType 0 \
    --EvidenceDescription 存证描述
```

Output: 
```
{
    "Response": {
        "EvidenceId": "eac6b301-a322-493a-8e36-83b295459397",
        "BusinessId": "as1111323311",
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

