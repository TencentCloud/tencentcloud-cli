**Example 1: 获取防护端口列表**



Input: 

```
tccli waf DescribePorts --cli-unfold-argument  \
    --InstanceID waf_2kw60zgy0908e8j3 \
    --Edition sparta-waf
```

Output: 
```
{
    "Response": {
        "HttpPorts": [
            "80",
            "8080"
        ],
        "HttpsPorts": [
            "443",
            "8443"
        ],
        "RequestId": "ae989097-a74b-448a-94e6-4e87366b173b"
    }
}
```

