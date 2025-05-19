**Example 1: Filter Name值不支持**

Filter Name只支持文档中的示例值

Input: 

```
tccli tke DescribeReservedInstances --cli-unfold-argument  \
    --Filters.0.Name not-support-filter-name \
    --Filters.0.Values value
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InternalError.Param",
            "Message": "Filter Name:not-support-filter-name not supported"
        },
        "RequestId": "b31166bd-80d6-4868-b13a-952bc1cdc74c"
    }
}
```

**Example 2: DescribeReservedInstances**

查询预留券列表

Input: 

```
tccli tke DescribeReservedInstances --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "ReservedInstanceSet": [],
        "RequestId": "a1be36f0-1aa4-4af2-a289-da021bcef89f"
    }
}
```

**Example 3: 支持的 Filter Name示例**

支持的 Filter Name示例

Input: 

```
tccli tke DescribeReservedInstances --cli-unfold-argument  \
    --Filters.0.Name status \
    --Filters.0.Values Active \
    --Filters.1.Name scope \
    --Filters.1.Values ap-guangzhou-2 \
    --Filters.2.Name cluster-id \
    --Filters.2.Values cls-3dkzu9z2 \
    --Filters.3.Name node-name \
    --Filters.3.Values eklet-subnet-9hxmgam6-790879 \
    --Filters.4.Name cpu \
    --Filters.4.Values 2 \
    --Filters.5.Name memory \
    --Filters.5.Values 4 \
    --Filters.6.Name resource-type \
    --Filters.6.Values common \
    --Filters.7.Name gpu \
    --Filters.7.Values  \
    --Filters.8.Name reserved-instance-id \
    --Filters.8.Values eksri-f9rwc82i \
    --Filters.9.Name reserved-instance-name \
    --Filters.9.Values c \
    --Filters.10.Name reserved-instance-not-deduct \
    --OrderField ExpireAt \
    --OrderDirection ASC
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "ReservedInstanceSet": [],
        "RequestId": "a1be36f0-1aa4-4af2-a289-da021bcef89f"
    }
}
```

**Example 4: 查询可用区范围的预留券**

只查询可用区抵扣的需要设置cluster-id和node-name 为空字符串

Input: 

```
tccli tke DescribeReservedInstances --cli-unfold-argument  \
    --Filters.0.Name status \
    --Filters.0.Values Active \
    --Filters.1.Name scope \
    --Filters.1.Values ap-guangzhou-2 \
    --Filters.2.Name cluster-id \
    --Filters.2.Values  \
    --Filters.3.Name node-name \
    --Filters.3.Values 
```

Output: 
```
{
    "Response": {
        "RequestId": "e49fe7f4-16f3-4640-839d-514edd3e897a",
        "ReservedInstanceSet": [],
        "TotalCount": 0
    }
}
```

**Example 5: 查询地域抵扣范围预留券**

查询地域抵扣范围预留券

Input: 

```
tccli tke DescribeReservedInstances --cli-unfold-argument  \
    --Filters.0.Name status \
    --Filters.0.Values Active \
    --Filters.1.Name scope \
    --Filters.1.Values 
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "ReservedInstanceSet": [],
        "RequestId": "a1be36f0-1aa4-4af2-a289-da021bcef89f"
    }
}
```

**Example 6: 查询节点抵扣范围的预留券**

查询节点抵扣范围的预留券

Input: 

```
tccli tke DescribeReservedInstances --cli-unfold-argument  \
    --Filters.0.Name status \
    --Filters.0.Values Active \
    --Filters.1.Name scope \
    --Filters.1.Values ap-guangzhou-2 \
    --Filters.2.Name cluster-id \
    --Filters.2.Values cls-3dkzu9z2 \
    --Filters.3.Name node-name \
    --Filters.3.Values eklet-subnet-9hxmgam6-790879
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "ReservedInstanceSet": [],
        "RequestId": "a1be36f0-1aa4-4af2-a289-da021bcef89f"
    }
}
```

