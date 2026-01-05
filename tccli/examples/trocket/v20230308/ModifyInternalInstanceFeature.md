**Example 1: 开启Topic&Group粒度鉴权配置**

开启Topic&Group粒度鉴权配置

Input: 

```
tccli trocket ModifyInternalInstanceFeature --cli-unfold-argument  \
    --ResourceId rmq-4k4orqgq \
    --Feature DetailedAcl \
    --Enable True
```

Output: 
```
{
    "Response": {
        "RequestId": "47d7fe3d-67d5-4e80-bcef-f2dc78018266"
    }
}
```

