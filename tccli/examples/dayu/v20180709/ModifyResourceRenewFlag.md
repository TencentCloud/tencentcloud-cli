**Example 1: Modifying the auto-renewal flag of resource**



Input: 

```
tccli dayu ModifyResourceRenewFlag --cli-unfold-argument  \
    --Business bgpip \
    --Id bgpip-000000x7 \
    --RenewFlag 1
```

Output: 
```
{
    "Response": {
        "Success": {
            "Code": "Success",
            "Message": "Success"
        },
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

