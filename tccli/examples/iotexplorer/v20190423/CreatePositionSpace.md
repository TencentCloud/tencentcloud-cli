**Example 1: CreatePositionSpace**

创建位置空间

Input: 

```
tccli iotexplorer CreatePositionSpace --cli-unfold-argument  \
    --ProjectId ProjectId \
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
        "SpaceId": "SpaceId",
        "RequestId": "f92406b3-5a9a-4fe8-bc43-45e3d794bb68"
    }
}
```

