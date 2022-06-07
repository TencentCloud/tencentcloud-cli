**Example 1: 生成普通码包**

生成普通码包

Input: 

```
tccli trp CreateCodePack --cli-unfold-argument  \
    --MerchantId eqdmnz7020bmtvi9 \
    --Amount 10 \
    --CodeLength 18 \
    --CodeType number \
    --PackType 0
```

Output: 
```
{
    "Response": {
        "PackId": "i655d7d68dzbbc4edi",
        "RequestId": "384f8d0c-0c15-4dce-9b23-85ca839364ad"
    }
}
```

