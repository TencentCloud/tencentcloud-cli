**Example 1: 业务数据明文存证**

用户通过本接口向BTOE写入待存证的业务数据明文。

Input: 

```
tccli btoe CreateDataDeposit --cli-unfold-argument  \
    --BusinessId as1111323311 \
    --EvidenceInfo 业务数据明文 \
    --EvidenceName 存证名称 \
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

