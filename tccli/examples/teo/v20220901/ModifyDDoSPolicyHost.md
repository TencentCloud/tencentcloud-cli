**Example 1: 域名高可用开启关闭**



Input: 

```
tccli teo ModifyDDoSPolicyHost --cli-unfold-argument  \
    --AccelerateType on \
    --SecurityType on \
    --Host a.eotest.com \
    --PolicyId 1 \
    --ZoneId zone-fawj94jag
```

Output: 
```
{
    "Response": {
        "RequestId": "faw89a4j0ag-awhf9aj-faj82agnmoa"
    }
}
```

