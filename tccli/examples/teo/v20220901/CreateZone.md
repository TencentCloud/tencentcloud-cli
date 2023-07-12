**Example 1: 创建站点**

正常创建站点。

Input: 

```
tccli teo CreateZone --cli-unfold-argument  \
    --JumpStart False \
    --Type full \
    --ZoneName example.com \
    --AllowDuplicates False \
    --AliasZoneName zone-example
```

Output: 
```
{
    "Response": {
        "ZoneId": "zone-27q0p0bali16",
        "RequestId": "2ccgtb24-7dc5-46s2-9r3e-95825d53dwe3a"
    }
}
```

