**Example 1: 查询密钥对列表**

本示例用于用户查询密钥对列表

Input: 

```
tccli cvm DescribeKeyPairs --cli-unfold-argument  \
    --Filters.0.Name key-name \
    --Filters.0.Values Tencent \
    --Offset 0 \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "KeyPairSet": [
            {
                "KeyId": "skey-mv9yzyjj",
                "KeyName": "Tencent",
                "Description": "",
                "PublicKey": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAAAgQDP0Yw2T4itUKOJQIK69c1Asy1UO88cxEbujR5Jbr0e/Ey1v4ZKAUzDnsBnFlf4hKPA1YvMB8RBYj4GcLtM7PrKnBNNram8rgl73X/klOO8oqKv+J/XUA7KHH1Y6wcn1RTRTMdDHbGhW1q/UpfeylNTbf+wEIWhEfaL5FKQm4hqCw== skey_112168",
                "AssociatedInstanceIds": [],
                "CreatedTime": "2016-12-02T00:22:40Z"
            }
        ],
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
    }
}
```

