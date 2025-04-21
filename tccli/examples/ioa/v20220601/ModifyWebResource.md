**Example 1: 修改web资源**

修改web资源

Input: 

```
tccli ioa ModifyWebResource --cli-unfold-argument  \
    --AreaId 3963 \
    --ConnectorGroupId cd6b2jdh2odn7arq90vg \
    --ServiceName 23 \
    --BackendPath / \
    --ServicePort 80 \
    --FrontHost 23 \
    --ServiceId 4387 \
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
        "RequestId": "9a96eb76-4030-4b55-a61a-c706bd257812"
    }
}
```

