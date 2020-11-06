**Example 1: Modifying DDoS protection status**



Input: 

```
tccli dayu ModifyDDoSDefendStatus --cli-unfold-argument  \
    --Business bgpip \
    --Id bgpip-000000xe \
    --Status 0 \
    --Hour 2
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

