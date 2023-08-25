**Example 1: 获取分类树信息**

获取分类树信息

Input: 

```
tccli dsgc DescribeDSPACategoryTree --cli-unfold-argument  \
    --DspaId dspa-001 \
    --ComplianceId 1
```

Output: 
```
{
    "Response": {
        "RequestId": "128009ac-7df4-0530-cc92-52f0d945e191",
        "ResultJson": "[{\"Id\":163,\"Name\":\"一级分类\",\"ComplianceId\":5,\"ParentId\":-1,\"IsLeaf\":1,\"Source\":1,\"Grade\":1,\"Rules\":null,\"Children\":[{\"Id\":164,\"Name\":\"二级分类\",\"ComplianceId\":5,\"ParentId\":163,\"IsLeaf\":0,\"Source\":1,\"Grade\":2,\"Rules\":null,\"Children\":[{\"Id\":165,\"Name\":\"三级分类1\",\"ComplianceId\":5,\"ParentId\":164,\"IsLeaf\":1,\"Source\":1,\"Grade\":3,\"Rules\":null,\"Children\":null},{\"Id\":166,\"Name\":\"三级分类2\",\"ComplianceId\":5,\"ParentId\":164,\"IsLeaf\":0,\"Source\":1,\"Grade\":3,\"Rules\":null,\"Children\":[{\"Id\":168,\"Name\":\"四级分类1\",\"ComplianceId\":5,\"ParentId\":166,\"IsLeaf\":0,\"Source\":1,\"Grade\":4,\"Rules\":null,\"Children\":null},{\"Id\":169,\"Name\":\"四级分类3\",\"ComplianceId\":5,\"ParentId\":166,\"IsLeaf\":0,\"Source\":1,\"Grade\":4,\"Rules\":null,\"Children\":[{\"Id\":170,\"Name\":\"五级分类3\",\"ComplianceId\":5,\"ParentId\":169,\"IsLeaf\":0,\"Source\":1,\"Grade\":5,\"Rules\":null,\"Children\":null}]}]},{\"Id\":167,\"Name\":\"三级分类3\",\"ComplianceId\":5,\"ParentId\":164,\"IsLeaf\":0,\"Source\":1,\"Grade\":3,\"Rules\":null,\"Children\":[{\"Id\":172,\"Name\":\"四级分类5\",\"ComplianceId\":5,\"ParentId\":167,\"IsLeaf\":1,\"Source\":1,\"Grade\":4,\"Rules\":null,\"Children\":null}]},{\"Id\":171,\"Name\":\"五级分类2\",\"ComplianceId\":5,\"ParentId\":164,\"IsLeaf\":1,\"Source\":1,\"Grade\":3,\"Rules\":null,\"Children\":null}]}]}]"
    }
}
```

