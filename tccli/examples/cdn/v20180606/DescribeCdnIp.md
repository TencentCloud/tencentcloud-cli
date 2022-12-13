**Example 1: IP 归属查询**



Input: 

```
tccli cdn DescribeCdnIp --cli-unfold-argument  \
    --Ips 1.1.1.1
```

Output: 
```
{
    "Response": {
        "RequestId": "156bde25-56b5-4dae-9638-b7b08b08e4f6",
        "Ips": [
            {
                "City": "shanghai",
                "Ip": "1.1.1.1",
                "Platform": "no",
                "Location": "unknown",
                "Area": "unknown",
                "History": []
            }
        ]
    }
}
```

