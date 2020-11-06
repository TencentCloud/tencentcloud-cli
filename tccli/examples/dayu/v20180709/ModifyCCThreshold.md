**Example 1: Modifying CC protection threshold**



Input: 

```
tccli dayu ModifyCCThreshold --cli-unfold-argument  \
    --Business bgpip \
    --Id bgpip-000000xe \
    --Threshold 1000
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

