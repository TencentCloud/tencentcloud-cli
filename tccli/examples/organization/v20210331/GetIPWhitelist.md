**Example 1: GetIPWhitelist**

GetIPWhitelist

Input: 

```
tccli organization GetIPWhitelist --cli-unfold-argument  \
    --ZoneId z-dh5i84h***
```

Output: 
```
{
    "Response": {
        "IpWhitelist": [
            "88.88.88.88",
            "11.179.212.0",
            "21.36.103.0",
            "8.8.9.9",
            "8.8.8.99"
        ],
        "RequestId": "c3142b5b-6963-40bd-a97e-5ec0fa15fa24"
    }
}
```

