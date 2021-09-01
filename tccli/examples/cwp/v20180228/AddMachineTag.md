**Example 1: 增加机器关联标签**

增加机器关联标签

Input: 

```
tccli cwp AddMachineTag --cli-unfold-argument  \
    --Quuid 2b6e5770-8e4d-11e9-8127-98be94219792 \
    --TagId 12 \
    --MRegion ap-guangzhou \
    --MArea CVM
```

Output: 
```
{
    "Response": {
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a"
    }
}
```

