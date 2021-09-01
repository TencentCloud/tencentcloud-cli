**Example 1: 文档存证**

用户通过本接口向BTOE写入待存证的文档原文件或下载URL，BTOE对文档原文件存储后，将其Hash值存证上链。

Input: 

```
tccli btoe CreateDocDeposit --cli-unfold-argument  \
    --BusinessId as1111323311 \
    --EvidenceName 存证名称 \
    --FileContent  \
    --FileName  \
    --FileUrl https: //cloud.tencent.com/document/product/1259/48506 \
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

