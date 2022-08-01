**Example 1: 修改通道组名称**



Input: 

```
tccli gaap ModifyProxyGroupAttribute --cli-unfold-argument  \
    --GroupName newName \
    --GroupId lg-b7h4d02f
```

Output: 
```
{
    "Response": {
        "RequestId": "19a021f8-dff3-4890-8e7a-ed5054e22e49"
    }
}
```

**Example 2: 修改通道组名**



Input: 

```
tccli gaap ModifyProxyGroupAttribute --cli-unfold-argument  \
    --GroupName test \
    --GroupId lg-pheemncl
```

Output: 
```
{
    "Response": {
        "RequestId": "e26d0984-af79-4403-8c51-11d075b7c1e8"
    }
}
```

