**Example 1: Querying client connections of a TencentDB instance**



Input: 

```
tccli mongodb DescribeClientConnections --cli-unfold-argument  \
    --InstanceId cmgo-eqmoaxxx
```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "Clients": [
            {
                "Count": 15,
                "IP": "10.xx.xx.xx"
            },
            {
                "Count": 15,
                "IP": "10.xx.xx.xx"
            }
        ],
        "RequestId": "c61fd6e2-c505-4fb9-9f30-edd8e897b236"
    }
}
```

