**Example 1: 根据CLB的VIP查询对应实例和客户信息**



Input: 

```
tccli ga2 DescribeClbVipInstances --cli-unfold-argument  \
    --IpAddress 3.1.2.192
```

Output: 
```
{
    "Response": {
        "InstanceSet": [
            {
                "AppId": "251201092",
                "GlobalAcceleratorId": "ga-gtae93tw",
                "IpAddress": "3.1.2.192",
                "Uin": "700000144096"
            }
        ],
        "RequestId": "bd039264-1999-4387-a563-c7c91a30a5b3"
    }
}
```

