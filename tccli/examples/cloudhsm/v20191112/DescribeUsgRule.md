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
        "TotalCount": 1,
        "SgRules": [
            {
                "Version": 0,
                "SgId": "UsgIdxxxxx",
                "SgName": "UsgNamexxxxxx",
                "SgRemark": "xxxxxxxx",
                "CreateTime": "2006-01-02 15:04:05",
                "InBound": [
                    {
                        "Ip": "xxxxx",
                        "Id": "xxxxxxx",
                        "AddressModule": "xxxxxx",
                        "Proto": "tcp",
                        "Port": "80",
                        "ServiceModule": "xxxxxx",
                        "Desc": "xxxxxx",
                        "Action": "DROP"
                    }
                ],
                "OutBound": [
                    {
                        "Ip": "xxxxx",
                        "Id": "xxxxxxx",
                        "AddressModule": "xxxxxx",
                        "Proto": "tcp",
                        "Port": "80",
                        "ServiceModule": "xxxxxx",
                        "Desc": "xxxxxx",
                        "Action": "DROP"
                    }
                ]
            }
        ],
        "RequestId": "6010cd3d-a85a-4e00-b37b-22606d017420"
    }
}
```

