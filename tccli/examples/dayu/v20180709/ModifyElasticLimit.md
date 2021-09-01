**Example 1: 修改弹性防护阈值**



Input: 

```
tccli dayu ModifyElasticLimit --cli-unfold-argument  \
    --Business bgpip \
    --Id bgpip-000000xe \
    --Limit 10000
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

