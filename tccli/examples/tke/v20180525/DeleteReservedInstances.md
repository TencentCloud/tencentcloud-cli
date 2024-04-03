**Example 1: 退还预留券实例**

同时会退还预留券相应的费用。

Input: 

```
tccli tke DeleteReservedInstances --cli-unfold-argument  \
    --ReservedInstanceIds eksri-epmr2bww
```

Output: 
```
{
    "Response": {
        "RequestId": "9d996a6f-5b4a-4e18-8fd1-cb258b2ce21f"
    }
}
```

**Example 2: 退还一个不存在的资源**

返回NotFound

Input: 

```
tccli tke DeleteReservedInstances --cli-unfold-argument  \
    --ReservedInstanceIds not-found
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "ResourceNotFound.NotFound",
            "Message": "resources:[]string{\"not-found\"} not found"
        },
        "RequestId": "e15cab8e-926a-4119-a4e5-208868d6821a"
    }
}
```

