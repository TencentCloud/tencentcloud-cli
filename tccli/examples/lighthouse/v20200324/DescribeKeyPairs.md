**Example 1: 查询用户密钥对列表**



Input: 

```
tccli lighthouse DescribeKeyPairs --cli-unfold-argument  \
    --KeyIds lhkp-omd12oc1
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "KeyPairSet": [
            {
                "KeyId": "lhkp-omd12oc1",
                "KeyName": "test",
                "PublicKey": "",
                "AssociatedInstanceIds": [],
                "CreatedTime": "2020-04-28T23:01:47Z",
                "PrivateKey": "null"
            }
        ],
        "RequestId": "9abb999a-53d6-4534-9b49-00e53b5c0fea"
    }
}
```

