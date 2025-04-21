**Example 1: 新增web资源**

新增web资源

Input: 

```
tccli ioa CreateWebResource --cli-unfold-argument  \
    --AreaId 3963 \
    --ConnectorGroupId cd6b2jdh2odn7arq90vg \
    --BackendPath / \
    --ServicePort 80 \
    --FrontHost 22 \
    --ServiceName 22 \
    --ServiceAddress iwenwiki.com \
    --FrontScheme http \
    --BackendScheme http \
    --FrontPath / \
    --WebGwResourceType 0
```

Output: 
```
{
    "Response": {
        "Data": {
            "ServiceId": 4387
        },
        "RequestId": "8079cd1d-4758-4139-968a-9545b68d6f1b"
    }
}
```

