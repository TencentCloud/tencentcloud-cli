**Example 1: 修改CC自定义策略开关**



Input: 

```
tccli dayu ModifyCCPolicySwitch --cli-unfold-argument  \
    --Business bgp \
    --Id bgp-000000xe \
    --SetId ccPolicy-000000sd \
    --Switch 0
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

