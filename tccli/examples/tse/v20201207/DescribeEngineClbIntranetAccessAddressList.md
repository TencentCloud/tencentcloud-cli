**Example 1: 查询引擎实例云梯环境下的CLB地址列表**



Input: 

```
tccli tse DescribeEngineClbIntranetAccessAddressList --cli-unfold-argument  \
    --InstanceId ins-xxx \
    --EngineRegion ap-beijing
```

Output: 
```
{
    "Response": {
        "Content": [
            {
                "VpcId": "vpc-123456",
                "SubnetId": "subnet-123456",
                "IntranetAddress": "10.1.0.1:2181",
                "Status": "normal",
                "Msg": ""
            }
        ],
        "RequestId": "3a2e00dd-1870-44b8-8b45-73ca8064ec47"
    }
}
```

