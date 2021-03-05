**Example 1: 素材列表**

拉起素材列表(对外)

Input: 

```
tccli facefusion DescribeMaterialList --cli-unfold-argument  \
    --ActivityId 10 \
    --MaterialId "q-materialId-000" \
    --Limit 10 \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "Count": 1,
        "RequestId": "testDescribeMaterialList1589864389240"
    }
}
```

