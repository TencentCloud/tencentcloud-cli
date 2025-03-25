**Example 1: 更新xmagic**

更新xmagic申请信息，  Status 为2，3的时候可用

Input: 

```
tccli vcube UpdateXMagic --cli-unfold-argument  \
    --XMagicResourceId xmc11671a6134d082bf79 \
    --CompanyPermit http://tencent.com/nengc.jpg \
    --CompanyType 娱乐 \
    --CompanyName nengc \
    --XMagicId 23487235
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

