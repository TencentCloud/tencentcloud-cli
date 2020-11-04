**Example 1: 查询PAI实例**

通过PAI实例ID查询

Input: 

```
tccli as DescribePaiInstances --cli-unfold-argument  \
    --InstanceIds ins-6he2sztp\
    --InnstanceIds ins-0xdrree5
```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "PaiInstanceSet": [
            {
                "InstanceId": "ins-6he2sztp",
                "BindingIp": "49.51.8.175",
                "DomainNameStatus": "ENABLED",
                "PaiMateUrl": "https://plumcot-j99466wb.pai.tcloudbase.com:5523",
                "DomainName": "plumcot-j99466wb.pai.tcloudbase.com"
            },
            {
                "InstanceId": "ins-0xdrree5",
                "BindingIp": "45.113.71.202",
                "DomainNameStatus": "ENABLED",
                "PaiMateUrl": "https://berry-kotucbu9.pai.tcloudbase.com:5523",
                "DomainName": "berry-kotucbu9.pai.tcloudbase.com"
            }
        ],
        "RequestId": "61a4c56f-c216-42f0-8238-eeabe338633e"
    }
}
```

