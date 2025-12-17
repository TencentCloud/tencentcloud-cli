**Example 1: DescribeMetadataObjectOwner示例**



Input: 

```
tccli tccatalog DescribeMetadataObjectOwner --cli-unfold-argument  \
    --MetadataObjectType FUNCTION \
    --FullName layyu_lakehouse.s1.f2
```

Output: 
```
{
    "Response": {
        "OwnerName": "",
        "OwnerType": "",
        "RequestId": "30e51454-8bfa-4c7b-b879-18306aac1ed9"
    }
}
```

