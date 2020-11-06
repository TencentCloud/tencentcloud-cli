**Example 1: 修改DDoS的防护等级**



Input: 

```
tccli dayu ModifyDDoSLevel --cli-unfold-argument  \
    --Business bgpip \
    --Id bgpip-000000xe \
    --Method set \
    --Level middle
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

