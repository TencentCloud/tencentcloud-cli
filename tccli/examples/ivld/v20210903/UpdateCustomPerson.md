**Example 1: 更新人物姓名与基本信息**



Input: 

```
tccli ivld UpdateCustomPerson --cli-unfold-argument  \
    --PersonId person-Axgo3FYc \
    --BasicInfo 新测试基本信息 \
    --Name 测试姓名B
```

Output: 
```
{
    "Response": {
        "PersonId": "person-Axgo3FYc",
        "RequestId": "78b360f1-fe7a-4576-8ab4-d48d06d44572"
    }
}
```

