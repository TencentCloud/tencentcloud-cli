**Example 1: test**



Input: 

```
tccli dlc DescribeNetworkConnections --cli-unfold-argument  \
    --NetworkConnectionType 4 \
    --DataEngineName  \
    --DatasourceConnectionVpcId  \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "NetworkConnectionSet": [],
        "RequestId": "4adde011-5462-4100-91db-ede860819fa6",
        "TotalCount": 0
    }
}
```

