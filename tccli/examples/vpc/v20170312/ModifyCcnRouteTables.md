**Example 1: 修改接口**



Input: 

```
tccli vpc ModifyCcnRouteTables --cli-unfold-argument  \
    --RouteTableInfo.0.RouteTableId ccnrtb-mnvhfmv9 \
    --RouteTableInfo.0.Name rubytest \
    --RouteTableInfo.0.Description ccnroutetable
```

Output: 
```
{
    "Response": {
        "RequestId": "ba7c7681-e051-469a-b0fc-210a373490a4"
    }
}
```

