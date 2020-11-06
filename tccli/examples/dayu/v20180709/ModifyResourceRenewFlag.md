**Example 1: 修改资源自动续费标记**



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

