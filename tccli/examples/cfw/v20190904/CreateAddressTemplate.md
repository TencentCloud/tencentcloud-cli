**Example 1: 创建地址模板**



Input: 

```
tccli cfw CreateAddressTemplate --cli-unfold-argument  \
    --Name 测试地址模板 \
    --Detail 测试地址模板 \
    --IpString 1.1.1.1 \
    --Type 0
```

Output: 
```
{
    "Response": {
        "Status": 0,
        "RequestId": "ped5452f-5619-4aad-8db6-cbc8bcda4b3c"
    }
}
```

