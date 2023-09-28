**Example 1: Scope 输入错误示例**

Scope 输入错误示例

Input: 

```
tccli tke ModifyReservedInstanceScope --cli-unfold-argument  \
    --ReservedInstanceIds eksri-762dtf76 \
    --ReservedInstanceScope.Scope regio
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InternalError.Param",
            "Message": "Scope must be in [Region, Zone, Node]"
        },
        "RequestId": "e88f8640-0e36-4154-a3bf-907b01aa62f0"
    }
}
```

**Example 2: 抵扣范围为地域**

设置预留券抵扣范围为地域

Input: 

```
tccli tke ModifyReservedInstanceScope --cli-unfold-argument  \
    --ReservedInstanceIds eksri-762dtf76 \
    --ReservedInstanceScope.Scope Region
```

Output: 
```
{
    "Response": {
        "RequestId": "9544ca07-e5da-4bde-8c27-807cf018e2f5"
    }
}
```

**Example 3: 设置抵扣范围为可用区**

抵扣范围为可用区时，Zone 必传，如：ap-guangzhou-2

Input: 

```
tccli tke ModifyReservedInstanceScope --cli-unfold-argument  \
    --ReservedInstanceIds eksri-762dtf76 \
    --ReservedInstanceScope.Scope Zone
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InternalError.Param",
            "Message": "Zone invalid"
        },
        "RequestId": "e949558d-f637-4223-8305-047cb2d5bf06"
    }
}
```

**Example 4: 设置抵扣范围为节点**

设置抵扣范围为节点

Input: 

```
tccli tke ModifyReservedInstanceScope --cli-unfold-argument  \
    --ReservedInstanceIds eksri-762dtf76 \
    --ReservedInstanceScope.Scope Node \
    --ReservedInstanceScope.Zone ap-guangzhou-2 \
    --ReservedInstanceScope.ClusterId cls-3dkzu9z2 \
    --ReservedInstanceScope.NodeName eklet-subnet-f0ed0d6e-24k6ucw0
```

Output: 
```
{
    "Response": {
        "RequestId": "67a932f4-1823-4cea-a16b-0744828dc597"
    }
}
```

**Example 5: 资源 ID 不存在**

输入的资源 ID不存在

Input: 

```
tccli tke ModifyReservedInstanceScope --cli-unfold-argument  \
    --ReservedInstanceIds eksri-762dtf7 \
    --ReservedInstanceScope.Scope region
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "ResourceNotFound.NotFound",
            "Message": "ReservedInstanceIds:[]string{\"eksri-762dtf7\"} not found"
        },
        "RequestId": "134fa43d-83a5-4b8d-8ea9-293a96515b68"
    }
}
```

