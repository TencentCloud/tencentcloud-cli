**Example 1: 获取实例列表**



Input: 

```
tccli wedata DescribeInstanceList --cli-unfold-argument  \
    --Sort xx \
    --PageIndex 0 \
    --PageSize 0 \
    --CycleList xx \
    --ProjectId xx \
    --OwnerList xx \
    --SortCol xx \
    --TaskTypeList 0 \
    --StateList 0 \
    --InstanceType xx
```

Output: 
```
{
    "Response": {
        "Data": "XX",
        "RequestId": "xx"
    }
}
```

