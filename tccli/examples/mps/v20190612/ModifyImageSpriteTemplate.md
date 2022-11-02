**Example 1: 修改雪碧图模板**



Input: 

```
tccli mps ModifyImageSpriteTemplate --cli-unfold-argument  \
    --ColumnCount 10 \
    --Definition 10001 \
    --Name 雪碧图模板1 \
    --RowCount 5 \
    --SampleType Percent \
    --Height 96 \
    --Width 54 \
    --SampleInterval 10
```

Output: 
```
{
    "Response": {
        "RequestId": "12ae8d8e-dce3-4151-9d4b-5594145287e1"
    }
}
```

