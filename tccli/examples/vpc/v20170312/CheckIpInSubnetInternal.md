**Example 1: 用于检查某个IP是否在子网里面**



Input: 

```
tccli vpc CheckIpInSubnetInternal --cli-unfold-argument  \
    --SubnetId 123123 \
    --Ip 2.2.2.2 1.1.1.1 \
    --UniqueSubnetId subnet-xxxx
```

Output: 
```
{
    "Response": {
        "CheckIpInSubnetResult": [
            {
                "Ip": "10.4.128.0",
                "CheckCode": 302
            },
            {
                "Ip": "10.4.127.0",
                "CheckCode": 301
            }
        ],
        "RequestId": "1b2534de-3f38-4913-921a-af5ff1a9cb73"
    }
}
```

