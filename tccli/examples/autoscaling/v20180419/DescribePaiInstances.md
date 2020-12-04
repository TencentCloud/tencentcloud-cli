**Example 1: 查询PAI实例**

通过PAI实例ID查询

Input: 

```
tccli as DescribePaiInstances --cli-unfold-argument  \
    --InstanceIds ins-6he2sztp ins-0xdrree5
```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "PaiInstanceSet": [
            {
                "InstanceId": "ins-6he2sztp",
                "PaiMateUrl": "https://plumcot-j99466wb.pai.tcloudbase.com:5523",
                "DomainName": "plumcot-j99466wb.pai.tcloudbase.com"
            },
            {
                "InstanceId": "ins-0xdrree5",
                "PaiMateUrl": "https://berry-kotucbu9.pai.tcloudbase.com:5523",
                "DomainName": "berry-kotucbu9.pai.tcloudbase.com"
            }
        ],
        "RequestId": "61a4c56f-c216-42f0-8238-eeabe338633e"
    }
}
```

