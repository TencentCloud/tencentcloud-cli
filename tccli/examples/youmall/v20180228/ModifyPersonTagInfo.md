**Example 1: 设置顾客身份**



Input: 

```
tccli youmall ModifyPersonTagInfo --cli-unfold-argument  \
    --CompanyId tencent \
    --ShopId 10086 \
    --Tags.0.OldType 0 \
    --Tags.0.NewType 2 \
    --Tags.0.PersonId 10
```

Output: 
```
{
    "Response": {
        "RequestId": "fbedb77c-66c4-4472-a4b2-f2b8890a8bac"
    }
}
```

