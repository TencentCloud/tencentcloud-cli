**Example 1: 创建源站组**



Input: 

```
tccli teo CreateOriginGroup --cli-unfold-argument  \
    --ZoneId zone-xxx \
    --OriginName oname \
    --Type weight \
    --OriginType self \
    --Record.0.Record 1.2.3.4 \
    --Record.0.Weight 50 \
    --Record.0.Port 10 \
    --Record.1.Record 123123123.com.com.cn \
    --Record.1.Weight 50 \
    --Record.1.Port 10
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "OriginId": "origin-xxx"
    }
}
```

