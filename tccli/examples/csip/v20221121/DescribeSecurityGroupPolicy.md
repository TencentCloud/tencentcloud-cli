**Example 1: 安全组策略**



Input: 

```
tccli csip DescribeSecurityGroupPolicy --cli-unfold-argument  \
    --Provider tencent \
    --AssetID i*s-**srzm2s \
    --AssetType cvm_instance \
    --MemberId mem-0acb10*2f**4**ee \
    --SecurityGroupID sg-lm**v9**
```

Output: 
```
{
    "Response": {
        "Egress": [
            {
                "Action": "ACCEPT",
                "CidrBlock": "0.0.0.0/0",
                "Description": "",
                "Port": "ALL",
                "Protocol": "ALL"
            }
        ],
        "Ingress": [
            {
                "Action": "ACCEPT",
                "CidrBlock": "0.0.0.0/0",
                "Description": "放*Wi**ows***录",
                "Port": "3389",
                "Protocol": "TCP"
            }
        ],
        "SecurityGroupIDList": [
            "sg-i*h*h*cw"
        ],
        "RequestId": "60f2de55-2df4-4e06-9564-6afe4bb1fd7b"
    }
}
```

