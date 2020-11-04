**Example 1: 调用返回成功**



Input: 

```
tccli fmu DeleteModel --cli-unfold-argument  \
    --ModelId xxxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

**Example 2: 调用返回失败**



Input: 

```
tccli fmu DeleteModel --cli-unfold-argument  \
    --ModelId xxxxx
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InvalidParameterValue.ModelIdNotFound",
            "Message": "未查找到素材id。"
        },
        "RequestId": "9208c1e0-d2e2-493f-9a46-299c02824625"
    }
}
```

