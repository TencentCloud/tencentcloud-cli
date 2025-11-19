**Example 1: 传统型NAT实例升级到标准型NAT**

传统型NAT实例升级到标准型NAT

Input: 

```
tccli vpc UpgradeNatGatewayProductVersion --cli-unfold-argument  \
    --VpcId vpc-2d98uyh6 \
    --NatGatewayId nat-lz6rjk7n \
    --Force 1
```

Output: 
```
{
    "Response": {
        "RequestId": "d9b0cd80-3b86-4e03-8fc9-bc7de311bc73"
    }
}
```

**Example 2: 校验传统型NAT实例能否升级到标准型NAT**

校验传统型NAT实例能否升级到标准型NAT
返回值无报错，表示校验成功。

Input: 

```
tccli vpc UpgradeNatGatewayProductVersion --cli-unfold-argument  \
    --VpcId vpc-2d98uyh6 \
    --NatGatewayId nat-lz6rjk7n \
    --Force 1 \
    --CheckOnlyMode true
```

Output: 
```
{
    "Response": {
        "RequestId": "d9b0cd80-3b86-4e03-8fc9-bc7de311bc73"
    }
}
```

