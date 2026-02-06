**Example 1: 开通云托管环境**



Input: 

```
tccli tcbr CreateCloudRunEnv --cli-unfold-argument  \
    --EnvId lowcode-xxxxxxxxxx \
    --PackageType Trial \
    --Source weda \
    --Channel weda \
    --Alias default
```

Output: 
```
{
    "Response": {
        "EnvId": "lowcode-xxxxxxxxxx",
        "RequestId": "c8b68d5a-d045-4740-b731-xxxxxxx",
        "TranId": ""
    }
}
```

