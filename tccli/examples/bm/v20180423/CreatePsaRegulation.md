**Example 1: 创建预授权规则**



Input: 

```
tccli bm CreatePsaRegulation --cli-unfold-argument  \
    --PsaName aaa \
    --PsaDescription bbb \
    --RepairLimit 66 \
    --TaskTypeIds 44
```

Output: 
```
{
    "Response": {
        "PsaId": "123",
        "RequestId": "a2a13989-5776-4a8b-83d6-43714117ac3c"
    }
}
```

