**Example 1: 查询dspm字典信息列表**



Input: 

```
tccli csip DescribeDspmDictionaryList --cli-unfold-argument  \
    --DictType IdentifyRule
```

Output: 
```
{
    "Response": {
        "DataSet": [
            {
                "DictId": 5800,
                "DictName": "姓名"
            }
        ],
        "RequestId": "cf839eee-b651-4ff3-9b49-173f9f55733f"
    }
}
```

