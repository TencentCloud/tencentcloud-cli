**Example 1: 检查用户地址联通性**



Input: 

```
tccli monitor CheckAddressByPrometheus --cli-unfold-argument  \
    --InstanceId prom-test \
    --Target http://1.1.1.1:1111/test
```

Output: 
```
{
    "Response": {
        "Target": "1.1.1.1:1111",
        "Success": true,
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

