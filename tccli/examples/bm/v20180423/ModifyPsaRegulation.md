**Example 1: 修改规则信息及关联故障类型**



Input: 

```
tccli bm ModifyPsaRegulation --cli-unfold-argument  \
    --PsaId 123 \
    --PsaName newname \
    --PsaDescription aaa
```

Output: 
```
{
    "Response": {
        "RequestId": "a2a13989-5776-4a8b-83d6-43714117ac3c"
    }
}
```

