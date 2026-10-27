**Example 1: RemoveDataDisks**



Input: 

```
tccli cvd RemoveDataDisks --cli-unfold-argument  \
    --InstanceId cdi-i71kxu6t60auxxxx \
    --DataDiskIds disk-swefdwdw
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

**Example 2: 卸载数据盘示例**



Input: 

```
tccli cvd RemoveDataDisks --cli-unfold-argument  \
    --InstanceId cdi-ubnpcatzru20umw \
    --DataDiskIds disk-c913zt0p
```

Output: 
```
{
    "Response": {
        "RequestId": "a0f470bc-70f1-4da1-83b6-7d5bd3f9bf6c"
    }
}
```

