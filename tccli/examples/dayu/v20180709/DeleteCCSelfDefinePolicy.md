**Example 1: 删除CC自定义策略**



Input: 

```
tccli dayu DeleteCCSelfDefinePolicy --cli-unfold-argument  \
    --Business bgp \
    --Id bgp-000000xe \
    --SetId ccPolicy-000000sd
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397",
        "Success": {
            "Code": "Success",
            "Message": "Success"
        }
    }
}
```

