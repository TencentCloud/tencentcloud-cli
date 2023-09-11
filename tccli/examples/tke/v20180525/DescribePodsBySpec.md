**Example 1: 查询满足规格的 Pod 信息**

可被预留券抵扣的 Pod 信息

Input: 

```
tccli tke DescribePodsBySpec --cli-unfold-argument  \
    --Cpu 1 \
    --Memory 2
```

Output: 
```
{
    "Response": {
        "PodSet": [],
        "RequestId": "3bd23fef-56bf-4d61-a2f2-5ea6adef1508",
        "TotalCount": 0
    }
}
```

**Example 2: Filter Name值不支持**

Filter Name只支持文档中的示例值

Input: 

```
tccli tke DescribePodsBySpec --cli-unfold-argument  \
    --Cpu 1 \
    --Memory 2 \
    --Filters.0.Name not-support-filter-name
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InternalError.Param",
            "Message": "Filter Name:not-support-filter-name not supported"
        },
        "RequestId": "3323e599-cc1f-481b-95a7-dec3f145d158"
    }
}
```

**Example 3: 不传 Filter 时默认查 intel 类型的 Pod 列表**

可通过 Filter中的 pod-type 指定查询某些类型的 Pod

Input: 

```
tccli tke DescribePodsBySpec --cli-unfold-argument  \
    --Cpu 1 \
    --Memory 2
```

Output: 
```
{
    "Response": {
        "PodSet": [
            {
                "ClusterId": "cls-3dkzu9z2",
                "Name": "nginx-6456b5b94c-8z5c5",
                "Namespace": "default",
                "NodeName": "eklet-subnet-f0ed0d6e-24k6ucw0",
                "Zone": "ap-guangzhou-2"
            }
        ],
        "RequestId": "3ee798bf-2e16-437a-8248-b00bf8113729",
        "TotalCount": 1
    }
}
```

**Example 4: 查询指定规格类型为 intel 的所有 pod 列表**

查询指定规格类型为 intel 的所有 pod 列表

Input: 

```
tccli tke DescribePodsBySpec --cli-unfold-argument  \
    --Cpu 1 \
    --Memory 2 \
    --Filters.0.Name pod-type \
    --Filters.0.Values intel
```

Output: 
```
{
    "Response": {
        "PodSet": [
            {
                "ClusterId": "cls-3dkzu9z2",
                "Name": "nginx-6456b5b94c-8z5c5",
                "Namespace": "default",
                "NodeName": "eklet-subnet-f0ed0d6e-24k6ucw0",
                "Zone": "ap-guangzhou-2"
            }
        ],
        "RequestId": "850b62dd-7f50-49f5-97df-1a960d3d6360",
        "TotalCount": 1
    }
}
```

