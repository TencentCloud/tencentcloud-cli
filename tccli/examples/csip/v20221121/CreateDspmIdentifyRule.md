**Example 1: 创建dspm数据识别数据项**



Input: 

```
tccli csip CreateDspmIdentifyRule --cli-unfold-argument  \
    --Name kyrie-kv-rule-004 \
    --Status 1 \
    --StructuredRule 1 \
    --UnStructuredRule 1
```

Output: 
```
{
    "Response": {
        "Id": 10009,
        "RequestId": "d11e8f63-703e-436c-a321-6f19eb33ff08"
    }
}
```

