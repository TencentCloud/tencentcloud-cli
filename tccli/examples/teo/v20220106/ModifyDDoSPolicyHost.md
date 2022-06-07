**Example 1: 域名高可用开启关闭**



Input: 

```
tccli teo ModifyDDoSPolicyHost --cli-unfold-argument  \
    --AccelerateType xx \
    --Host xx \
    --PolicyId 0 \
    --ZoneId xx
```

Output: 
```
{
    "Response": {
        "Host": "xx",
        "RequestId": "xx"
    }
}
```

