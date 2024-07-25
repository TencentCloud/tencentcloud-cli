**Example 1: 查询Nat防火墙Dnat规则**

查询Nat防火墙Dnat规则

Input: 

```
tccli cfw DescribeNatFwDnatRule --cli-unfold-argument  \
    --Index abc \
    --Filters.0.Name abc \
    --Filters.0.Values abc \
    --Filters.0.OperatorType 0 \
    --Limit 1 \
    --Offset 1 \
    --StartTime abc \
    --EndTime abc \
    --Order abc \
    --By abc
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Id": 0,
                "IpProtocol": "abc",
                "PublicIpAddress": "abc",
                "PublicPort": 0,
                "PrivateIpAddress": "abc",
                "PrivatePort": 0,
                "Description": "abc",
                "IsReferenced": 0,
                "FwInsId": "abc",
                "NatGwId": "abc"
            }
        ],
        "Total": 1,
        "RequestId": "abc"
    }
}
```

