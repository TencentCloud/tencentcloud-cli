**Example 1: 获取安全组详情**



Input: 

```
tccli cloudhsm DescribeUsgRule --cli-unfold-argument  \
    --SgIds xxxxxxxxxxxx
```

Output: 
```
{
    "Response": {
        "SgRules": [
            {
                "Version": 0,
                "UsgId": "UsgIdxxxxx",
                "UsgName": "UsgNamexxxxxx",
                "InBound": {
                    "Ip": "xxxxx",
                    "Id": "xxxxxxx",
                    "AddressModule": "xxxxxx",
                    "Proto": "tcp",
                    "Port": "80",
                    "ServiceModule": "xxxxxx",
                    "Desc": "xxxxxx",
                    "Action": "DROP"
                }
            }
        ],
        "RequestId": "6010cd3d-a85a-4e00-b37b-22606d017420"
    }
}
```

