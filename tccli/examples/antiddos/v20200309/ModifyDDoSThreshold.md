**Example 1: 修改DDoS清洗阈值**



Input: 

```
tccli antiddos ModifyDDoSThreshold --cli-unfold-argument  \
    --Threshold 1000 \
    --Id bgpip-000000xe \
    --Business bgpip
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

