**Example 1: Deleting an advanced DDoS protection policy**



Input: 

```
tccli dayu DeleteDDoSPolicy --cli-unfold-argument  \
    --Business bgpip\
    --PolicyId policy-000000xe
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

