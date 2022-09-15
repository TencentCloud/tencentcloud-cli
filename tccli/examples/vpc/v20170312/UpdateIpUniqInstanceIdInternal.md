**Example 1: 用于更新ip地址绑定的资源id**



Input: 

```
tccli vpc UpdateIpUniqInstanceIdInternal --cli-unfold-argument  \
    --UpdateIpUniqInstanceIdSet.0.OldUniqueInstanceId ins-asdasdas \
    --UpdateIpUniqInstanceIdSet.0.Ip 1.1.1.1 \
    --UpdateIpUniqInstanceIdSet.0.UniqueVpcId vpc-jmaywf6r \
    --UpdateIpUniqInstanceIdSet.0.VpcId 1 \
    --UpdateIpUniqInstanceIdSet.0.UniqueInstanceId ins-asdadas
```

Output: 
```
{
    "Response": {
        "UpdateIpUniqInstanceIdResult": [
            {
                "OriginUniqInstanceId": "cdb-czpmp66w",
                "VpcId": 1141,
                "UniqueVpcId": "vpc-puh8eykn",
                "Ip": "10.19.165.10",
                "UniqueInstanceId": "cdb-e2073faq"
            }
        ],
        "RequestId": "1b2534de-3f38-4913-921a-af5ff1a9cb73"
    }
}
```

