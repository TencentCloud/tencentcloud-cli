**Example 1: 查看实例hai-xxxxxxxx关联的公网配置及使用情况**

查看实例hai-xxxxxxxx关联的公网配置及使用情况

Input: 

```
tccli hai DescribeInstanceNetworkStatus --cli-unfold-argument  \
    --InstanceIds hai-jklfaded
```

Output: 
```
{
    "Response": {
        "TotalCount": 10,
        "NetworkStatusSet": [
            {
                "InstanceId": "hai-xxxxxxxx",
                "AddressIp": "1.1.1.1",
                "Bandwidth": 5,
                "TotalTrafficAmount": 1000,
                "RemainingTrafficAmount": 500
            }
        ],
        "RequestId": "41fa870d-8592-493c-b794-9fe19f23e800"
    }
}
```

