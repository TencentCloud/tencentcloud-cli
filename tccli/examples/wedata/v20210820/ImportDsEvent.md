**Example 1: 批量导入事件**

批量导入事件

Input: 

```
tccli wedata ImportDsEvent --cli-unfold-argument  \
    --ProjectId abc \
    --FileName events-20231109152058.csv
```

Output: 
```
{
    "Response": {
        "Data": true,
        "RequestId": "abc"
    }
}
```

