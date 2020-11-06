**Example 1: Modifying CC protection level**



Input: 

```
tccli dayu ModifyCCLevel --cli-unfold-argument  \
    --Business bgpip \
    --Id bgpip-000000xe \
    --Level default \
    --Protocol https \
    --RuleId rule-0000000x
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

