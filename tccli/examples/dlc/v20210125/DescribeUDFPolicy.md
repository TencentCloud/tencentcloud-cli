**Example 1: 获取UDF权限信息**



Input: 

```
tccli dlc DescribeUDFPolicy --cli-unfold-argument  \
    --Name myfunction \
    --DatabaseName global-function \
    --CatalogName DataLakeCatalog
```

Output: 
```
{
    "Response": {
        "RequestId": "4ffcb19d-e23a-4816-bdc2-d69bdc586a0d",
        "UDFPolicyInfos": [
            {
                "Accesses": [
                    "alter"
                ],
                "Users": [
                    "49830499352"
                ],
                "Groups": [
                    "221447"
                ]
            }
        ]
    }
}
```

