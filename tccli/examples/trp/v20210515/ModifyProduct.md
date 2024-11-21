**Example 1: 编辑商品**



Input: 

```
tccli trp ModifyProduct --cli-unfold-argument  \
    --Name demo5 \
    --ProductId 85tfp1sn78r9m1568i \
    --Remark 商品备注 \
    --Specification 100ml \
    --Logo https://xxx.xxx.com/logo.png
```

Output: 
```
{
    "Response": {
        "ProductId": "85tfp1sn78r9m1568i",
        "RequestId": "43ad9b9f-ccc0-4051-a482-34da3422ceab"
    }
}
```

