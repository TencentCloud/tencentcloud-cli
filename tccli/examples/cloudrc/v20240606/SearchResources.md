**Example 1: 查询广州的资源**



Input: 

```
tccli cloudrc SearchResources --cli-unfold-argument  \
    --Filters.0.Key RegionCode \
    --Filters.0.Values ap-guangzhou
```

Output: 
```
{
    "Response": {
        "NextToken": "cCuk41e5JoaacP6PzhydNNStUM5couVJsUY7klW3qet5afBsukPVCXcoxUCPUKqjLbDDjuaDL3cC5XRuEeAMgi/I/niv6ZxB0DgTIxXnSqU4ehEYAKgHOR6uVc1aDaQnAKiuk4bOLqtxYuppLEd2N2WFoJrxLMUwvvX8Bw9DzXJ9zCHD5eD0oa81KYmKolmdAjViZfdi0kcvw4qv4uaTdzDEHoc=",
        "Resources": [
            {
                "CreateTime": "2017-12-05 15:28:22",
                "PayMode": "Free",
                "PrivateIpAddress": [],
                "PublicIpAddress": [],
                "RegionCode": "ap-guangzhou",
                "ResourceAlias": "******Test",
                "ResourceId": "vpc-m3ul053f",
                "ResourceType": "qcs::vpc::vpc",
                "Tags": [],
                "Uin": 909600000
            }
        ],
        "RequestId": "64ec7bde-2b9b-4b65-b66a-676a795d84ea"
    }
}
```

