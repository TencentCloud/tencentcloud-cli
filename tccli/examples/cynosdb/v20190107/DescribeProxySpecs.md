**Example 1: 查询数据库代理规格**



Input: 

```
tccli cynosdb DescribeProxySpecs --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "ProxySpecs": [
            {
                "Mem": 0,
                "Cpu": 0
            }
        ],
        "RequestId": "request-756112"
    }
}
```

**Example 2: 查询proxy规格**



Input: 

```
tccli cynosdb DescribeProxySpecs --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "ProxySpecs": [
            {
                "Cpu": 2,
                "Mem": 4000
            },
            {
                "Cpu": 4,
                "Mem": 8000
            },
            {
                "Cpu": 8,
                "Mem": 16000
            }
        ],
        "RequestId": "f4479b74-e428-40d9-a81f-e34cac00ae70"
    }
}
```

