**Example 1: 查询uin是否有效**

查询uin是否有效

Input: 

```
tccli bi CheckUinInfo --cli-unfold-argument  \
    --PartnerUin 123 \
    --PartnerSubUin 123 \
    --CustomerUin 456 \
    --CustomerId 123 \
    --CustomerName 机构1
```

Output: 
```
{
    "Response": {
        "Msg": "Uin 错误",
        "RequestId": "123",
        "Extra": "",
        "Data": null
    }
}
```

