**Example 1: UDF权限修改**



Input: 

```
tccli dlc UpdateUDFPolicy --cli-unfold-argument  \
    --Name table1 \
    --DatabaseName global-function \
    --CatalogName DataLakeCatalog \
    --UDFPolicyInfos.0.Accesses alter \
    --UDFPolicyInfos.0.Users 49830499352 \
    --UDFPolicyInfos.0.Groups 221447
```

Output: 
```
{
    "Response": {
        "RequestId": "05d2202d-d1b6-40af-8be3-9b1202ad8eb7",
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

