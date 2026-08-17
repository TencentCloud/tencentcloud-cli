**Example 1: 修改CVM复制对名称**



Input: 

```
tccli bdrc ModifyCopyPairAttribute --cli-unfold-argument  \
    --CopyPairId cvmcopypair-ifytsjpr \
    --CopyPairType INSTANCE \
    --CopyPairName new copy pair 3
```

Output: 
```
{
    "Response": {
        "RequestId": "fa6b373a-1b6a-42e7-af40-a7b23f49118a"
    }
}
```

