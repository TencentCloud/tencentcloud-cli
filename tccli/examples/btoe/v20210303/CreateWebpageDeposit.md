**Example 1: 网页快照存证**

用户通过本接口向BTOE提交待存证网页的URL，BTOE对URL进行网页快照，并将快照图片存储，将网页快照Hash值存证上链。

Input: 

```
tccli btoe CreateWebpageDeposit --cli-unfold-argument  \
    --BusinessId as1111323311 \
    --EvidenceName 网页存证名称 \
    --EvidenceUrl https: //cloud.tencent.com/document/product/1259/48506 \
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

**Example 2: 网页快照存证示例**



Input: 

```
tccli btoe CreateWebpageDeposit --cli-unfold-argument  \
    --HashType 0 \
    --EvidenceUrl https://www.xxxxxx.com/ \
    --EvidenceDescription 网页快照存证测试 \
    --EvidenceName 网页快照存证测试 \
    --BusinessId 47d5624a-41d4-4e7c-b99c-3172474073ba
```

Output: 
```
{
    "Response": {
        "RequestId": "23a2d753-13e3-4872-87b7-b609a46af01d",
        "EvidenceId": "23a2d753-13e3-4872-87b7-b609a46af01d",
        "BusinessId": "47d5624a-41d4-4e7c-b99c-3172474073ba"
    }
}
```

