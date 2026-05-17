**Example 1: 查询cos审计字典值**



Input: 

```
tccli csip DescribeCosAuditDictionaryList --cli-unfold-argument  \
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
        "RequestId": "ad346878-e03e-4945-9e90-7fd5e08fe677"
    }
}
```

