**Example 1: 获取子网内可用IP列表**

获取子网内可用IP列表

Input: 

```
tccli bmvpc DescribeSubnetAvailableIps --cli-unfold-argument  \
    --SubnetId subnet-q1j48dkd
```

Output: 
```
{
    "Response": {
        "IpSet": [
            "10.27.2.2",
            "10.27.2.5-10.27.2.15",
            "10.27.2.17-10.27.2.20",
            "10.27.2.22-10.27.2.254"
        ],
        "RequestId": "ff20d849-1137-423f-8be7-bca8bc1cb44a"
    }
}
```

