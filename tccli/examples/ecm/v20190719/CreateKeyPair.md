**Example 1: 创建密钥对**

创建密钥对

Input: 

```
tccli ecm CreateKeyPair --cli-unfold-argument  \
    --KeyName tencent
```

Output: 
```
{
    "Response": {
        "KeyPair": {
            "KeyId": "skey-mv9yzyjj",
            "Description": "",
            "CreatedTime": "2020-09-22T00:00:00+00:00",
            "KeyName": "Tencent",
            "AssociatedInstanceIds": [],
            "PrivateKey": "-----BEGIN RSA PRIVATE KEY-----\nMIICXgIBAAKBgQDP0Yw2T4itUKOJQIK69c1Asy1UO88cxEbujR5Jbr0e/Ey1v4ZK\nAUzDnsBnFlf4h***********************************niikSnZuZPNSw8T+kg\n/oxijESOLAJBnt3S/g+D530Enjitvfc9mEB7mh0VmwWvPg==\n-----END RSA PRIVATE KEY-----\n",
            "ProjectId": 0,
            "PublicKey": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAAAgQDP0Yw2T4itUKOJQIK69c1*******************************************+J/XUA7KHH1Y6wcn1RTRTMdDHbGhW1q/UpfeylNTbf+wEIWhEfaL5FKQm4hqCw== skey_112168"
        },
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
    }
}
```

