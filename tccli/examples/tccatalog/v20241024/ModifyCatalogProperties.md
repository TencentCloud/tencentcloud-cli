**Example 1: 修改数据目录属性**

修改数据目录属性

Input: 

```
tccli tccatalog ModifyCatalogProperties --cli-unfold-argument  \
    --CatalogId b8sd7dd7-ekd4-4e5e-993e-e5db64fa21c1 \
    --Properties.0.Key uri \
    --Properties.0.Value http://1.0.0.1:10001
```

Output: 
```
{
    "Response": {
        "RequestId": "b8sd7dd7-ekd4-4e5e-993e-e5db64fa21c1"
    }
}
```

