**Example 1: 创建云联网路由表**

创建云联网路由表

Input: 

```
tccli vpc CreateCcnRouteTables --cli-unfold-argument  \
    --RouteTable.0.CcnId ccn-8j0phqix \
    --RouteTable.0.Name rubytest \
    --RouteTable.0.Description test
```

Output: 
```
{
    "Response": {
        "CcnRouteTableSet": [
            {
                "CcnId": "ccn-8j0phqix",
                "CcnRouteTableId": "ccnrtb-mnvhfmv9",
                "RouteTableName": "rubytest",
                "RouteTableDescription": "test",
                "IsDefaultTable": true,
                "CreateTime": "2021-05-11 15:47:53"
            }
        ],
        "RequestId": "ba7c7681-e051-469a-b0fc-210a373490a4"
    }
}
```

