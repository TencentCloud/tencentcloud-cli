**Example 1: 修改数据库代理VIP或端口**



Input: 

```
tccli cdb ModifyCDBProxyVipVPort --cli-unfold-argument  \
    --DstIp 127.0.1 \
    --ProxyGroupId proxt-test \
    --UniqVpcId vpc-test \
    --UniqSubnetId sub-test \
    --ReleaseDuration 1 \
    --DstPort 1201
```

Output: 
```
{
    "Response": {
        "RequestId": "3689c0eb-a92d-77ce-0ee2-17d99f604e64"
    }
}
```

