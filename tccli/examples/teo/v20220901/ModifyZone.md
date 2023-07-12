**Example 1: 修改站点**

修改站点。

Input: 

```
tccli teo ModifyZone --cli-unfold-argument  \
    --VanityNameServers.Switch on \
    --VanityNameServers.Servers ns1.example.com ns2.example.com \
    --Type full \
    --ZoneId zone-27q0p0bali16 \
    --AliasZoneName zone-example
```

Output: 
```
{
    "Response": {
        "RequestId": "4ac50b24-7dc2-47f4-92ce-9fd25d53gt2f"
    }
}
```

