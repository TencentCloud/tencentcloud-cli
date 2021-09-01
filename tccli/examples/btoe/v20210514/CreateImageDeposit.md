**Example 1: 图片文件存证**

用户通过本接口向BTOE写入待存证的图片原文件或下载URL，BTOE对图片原文件存储后，将其Hash值存证上链。

Input: 

```
tccli btoe CreateImageDeposit --cli-unfold-argument  \
    --BusinessId as1111323311 \
    --EvidenceName 图片文件存证 \
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

