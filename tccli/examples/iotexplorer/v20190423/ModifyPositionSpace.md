**Example 1: 更新位置空间**



Input: 

```
tccli iotexplorer ModifyPositionSpace --cli-unfold-argument  \
    --SpaceId Id \
    --ProductIdList ProductId \
    --SpaceName space \
    --Description service \
    --Icon http://www.example.com \
    --AuthorizeType 0
```

Output: 
```
{
    "Response": {
        "RequestId": "f92406b3-5a9a-4fe8-bc43-45e3d794bb68"
    }
}
```

