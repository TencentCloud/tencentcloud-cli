**Example 1: 供应商拒单示例**

供应商拒单示例

Input: 

```
tccli subcontract RefusePrOrder --cli-unfold-argument  \
    --PoId PO11211023112631921661 \
    --Reason 拒单PO11211023112631921661
```

Output: 
```
{
    "Response": {
        "PoId": "PO11211023112631921661",
        "RequestId": "xx"
    }
}
```

