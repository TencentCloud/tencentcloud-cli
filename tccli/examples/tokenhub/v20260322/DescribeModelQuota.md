**Example 1: 正常请求**



Input: 

```
tccli tokenhub DescribeModelQuota --cli-unfold-argument  \
    --ModelId glm-5.2
```

Output: 
```
{
    "Response": {
        "ModelId": "glm-5.2",
        "RPMLimit": 601,
        "RequestId": "cfa39e4e-d23a-409b-9488-1a4de77a16e2",
        "TPMInputQuotaLimit": 20000000,
        "TPMInputReserveLimit": 10000000,
        "TPMLimit": 5000000,
        "TPMOutputQuotaLimit": 2000000,
        "TPMOutputReserveLimit": 1000000
    }
}
```

