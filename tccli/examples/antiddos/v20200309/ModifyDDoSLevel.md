**Example 1: 修改DDoS的防护等级**



Input: 

```
tccli antiddos ModifyDDoSLevel --cli-unfold-argument  \
    --Id bgpip-000000xe \
    --Business bgpip \
    --Method get
```

Output: 
```
{
    "Response": {
        "DDoSLevel": "middle",
        "Id": "bgpip-000000xe",
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

